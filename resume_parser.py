import spacy
import os
from file_handling import FileHandler


class ResumeParser:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")
        self.file_handler = FileHandler()

    def parse_resume(self, input_data, is_text=True):
        """
        Extracts text and key entities from a resume.
        
        Args:
            input_data (str): File path or raw resume text.
            is_text (bool): Set to True if input_data is raw text, False if it's a file path.
            
        Returns:
            dict: Extracted text and entities.
        """
        # If input is raw text
        if is_text:
            resume_text = input_data
            print("Processing raw text input...")
        
        # If input is a file path
        else:
            print("Processing file:", input_data)
            
            # Check if the file exists
            if not os.path.exists(input_data):
                raise FileNotFoundError(f"File not found: {input_data}")
            
            # Extract file extension
            file_extension = os.path.splitext(input_data)[1].lower()
            print("Detected extension:", file_extension)
            
            # Validate file extension
            if file_extension not in [".pdf", ".docx"]:
                raise ValueError(f"Unsupported file type: {file_extension}. Please provide a '.docx' or '.pdf' file.")
            
            # Extract text from the file
            resume_text = self.file_handler.extract_text(input_data)
        
        # Process text with NLP
        doc = self.nlp(resume_text)
        
        # Return extracted entities
        return {
            "text": resume_text,
            "entities": [(ent.text, ent.label_) for ent in doc.ents]
        }

if __name__ == "__main__":
    parser = ResumeParser()
    
    # Change this to the actual file path you are using

    
    try:
        result = parser.parse_resume()
        print(result)
    except Exception as e:
        print("Error:", e)
