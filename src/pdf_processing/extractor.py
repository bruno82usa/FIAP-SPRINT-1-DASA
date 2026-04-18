import pdfplumber
import pytesseract
from PIL import Image
import io
import re
import json
from typing import Dict, Any, Optional, List
import tempfile
import os


class PDFExtractor:
    def __init__(self, use_ocr: bool = True):
        self.use_ocr = use_ocr
        
    def extract_text(self, pdf_path: str) -> str:
        """
        Extract text from PDF using pdfplumber and optionally OCR
        """
        text = ""
        
        try:
            with pdfplumber.open(pdf_path) as pdf:
                for page in pdf.pages:
                    # Try to extract text directly
                    page_text = page.extract_text()
                    
                    # If no text found and OCR is enabled, try OCR
                    if not page_text and self.use_ocr:
                        page_text = self._extract_with_ocr(page)
                    
                    text += page_text + "\n\n"
                    
        except Exception as e:
            raise Exception(f"Error extracting text from PDF: {str(e)}")
        
        return text.strip()
    
    def _extract_with_ocr(self, page) -> str:
        """
        Extract text from page using OCR
        """
        try:
            # Convert page to image
            image = page.to_image(resolution=300)
            img_bytes = io.BytesIO()
            image.save(img_bytes, format='PNG')
            img_bytes.seek(0)
            
            # Use pytesseract for OCR
            img = Image.open(img_bytes)
            text = pytesseract.image_to_string(img, lang='por+eng')
            return text
            
        except Exception as e:
            print(f"OCR failed: {str(e)}")
            return ""
    
    def clean_text(self, text: str) -> str:
        """
        Clean extracted text by removing excessive whitespace and normalizing
        """
        # Replace multiple newlines with double newline
        text = re.sub(r'\n\s*\n+', '\n\n', text)
        
        # Replace multiple spaces with single space
        text = re.sub(r'\s+', ' ', text)
        
        # Remove page numbers and headers/footers
        text = re.sub(r'^\s*\d+\s*$', '', text, flags=re.MULTILINE)
        
        return text.strip()
    
    def identify_sections(self, text: str) -> Dict[str, str]:
        """
        Identify common sections in genetic reports
        """
        sections = {}
        
        # Common section headers in genetic reports
        section_patterns = {
            'patient_info': r'(?:Paciente|Patient|Informações Pessoais).*?(?=\n\n|\Z)',
            'genetic_risks': r'(?:Riscos Genéticos|Genetic Risks|Resultados).*?(?=\n\n|\Z)',
            'ancestry': r'(?:Ancestralidade|Ancestry|Origem).*?(?=\n\n|\Z)',
            'carrier_status': r'(?:Status de Portador|Carrier Status).*?(?=\n\n|\Z)',
            'pharmacogenomics': r'(?:Farmacogenômica|Drug Response).*?(?=\n\n|\Z)',
            'recommendations': r'(?:Recomendações|Recommendations).*?(?=\n\n|\Z)',
        }
        
        for section_name, pattern in section_patterns.items():
            match = re.search(pattern, text, re.IGNORECASE | re.DOTALL)
            if match:
                sections[section_name] = match.group(0).strip()
        
        return sections
    
    def extract_structured_data(self, text: str) -> Dict[str, Any]:
        """
        Extract structured data from text using regex patterns
        """
        data = {
            'metadata': {},
            'genetic_risks': [],
            'carrier_status': [],
            'ancestry': {},
            'pharmacogenomics': []
        }
        
        # Extract patient information
        patient_info = self._extract_patient_info(text)
        if patient_info:
            data['patient_info'] = patient_info
        
        # Extract genetic risks
        risks = self._extract_genetic_risks(text)
        if risks:
            data['genetic_risks'] = risks
        
        # Extract carrier status
        carriers = self._extract_carrier_status(text)
        if carriers:
            data['carrier_status'] = carriers
        
        # Extract ancestry information
        ancestry = self._extract_ancestry(text)
        if ancestry:
            data['ancestry'] = ancestry
        
        return data
    
    def _extract_patient_info(self, text: str) -> Optional[Dict[str, str]]:
        """Extract patient information"""
        patterns = {
            'name': r'Nome[:\s]+([A-Za-z\s]+)',
            'age': r'Idade[:\s]+(\d+)',
            'gender': r'Sexo[:\s]+([A-Za-z]+)',
            'id': r'ID[:\s]+([A-Za-z0-9\-]+)'
        }
        
        info = {}
        for key, pattern in patterns.items():
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                info[key] = match.group(1).strip()
        
        return info if info else None
    
    def _extract_genetic_risks(self, text: str) -> List[Dict[str, Any]]:
        """Extract genetic risk information"""
        risks = []
        
        # Look for risk patterns
        risk_pattern = r'([A-Za-z\s]+)\s*[:\.]\s*(?:Risco|Risk)[:\s]+([A-Za-z\s]+)'
        matches = re.finditer(risk_pattern, text, re.IGNORECASE)
        
        for match in matches:
            condition = match.group(1).strip()
            risk_level = match.group(2).strip()
            
            risks.append({
                'condition': condition,
                'risk_level': risk_level,
                'confidence': 0.85  # Default confidence
            })
        
        return risks
    
    def _extract_carrier_status(self, text: str) -> List[Dict[str, str]]:
        """Extract carrier status information"""
        carriers = []
        
        carrier_pattern = r'([A-Za-z\s]+)\s*[:\.]\s*(?:Portador|Carrier)[:\s]+([A-Za-z\s]+)'
        matches = re.finditer(carrier_pattern, text, re.IGNORECASE)
        
        for match in matches:
            condition = match.group(1).strip()
            status = match.group(2).strip()
            
            carriers.append({
                'condition': condition,
                'status': status,
                'gene': 'Unknown'  # Would be extracted from more detailed parsing
            })
        
        return carriers
    
    def _extract_ancestry(self, text: str) -> Dict[str, float]:
        """Extract ancestry composition"""
        ancestry = {}
        
        # Look for percentage patterns
        percent_pattern = r'([A-Za-z\s]+)[:\s]+([\d\.]+)%'
        matches = re.finditer(percent_pattern, text)
        
        for match in matches:
            region = match.group(1).strip()
            percentage = float(match.group(2))
            
            if percentage > 0:
                ancestry[region] = percentage
        
        return ancestry
    
    def process_pdf(self, pdf_path: str) -> Dict[str, Any]:
        """
        Complete PDF processing pipeline
        """
        # Extract raw text
        raw_text = self.extract_text(pdf_path)
        
        # Clean text
        clean_text = self.clean_text(raw_text)
        
        # Identify sections
        sections = self.identify_sections(clean_text)
        
        # Extract structured data
        structured_data = self.extract_structured_data(clean_text)
        
        return {
            'raw_text': raw_text[:1000] + '...' if len(raw_text) > 1000 else raw_text,
            'clean_text': clean_text[:1000] + '...' if len(clean_text) > 1000 else clean_text,
            'sections': sections,
            'structured_data': structured_data,
            'page_count': self._get_page_count(pdf_path),
            'processing_success': True
        }
    
    def _get_page_count(self, pdf_path: str) -> int:
        """Get number of pages in PDF"""
        try:
            with pdfplumber.open(pdf_path) as pdf:
                return len(pdf.pages)
        except:
            return 0


def extract_from_pdf_file(file_content: bytes, filename: str) -> Dict[str, Any]:
    """
    Helper function to process PDF from file content
    """
    # Create temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as tmp_file:
        tmp_file.write(file_content)
        tmp_path = tmp_file.name
    
    try:
        extractor = PDFExtractor()
        result = extractor.process_pdf(tmp_path)
        return result
    finally:
        # Clean up temporary file
        if os.path.exists(tmp_path):
            os.unlink(tmp_path)