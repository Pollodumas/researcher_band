import os
from dotenv import load_dotenv
from src.services.research_service import ResearchService
from src.utils.file_processor import FileProcessor

def main():
    load_dotenv()  # Load environment variables
    
    print("🔍 Blockchain Research System")
    print("-----------------------------")
    
    research_service = ResearchService()
    file_processor = FileProcessor()
    
    while True:
        print("\nOptions:")
        print("1. Analyze text input")
        print("2. Analyze URL")
        print("3. Analyze PDF file")
        print("4. Exit")
        
        choice = input("\nSelect an option (1-4): ")
        
        if choice == "4":
            print("Goodbye!")
            break
            
        try:
            content = ""
            if choice == "1":
                text = input("Enter your research text: ")
                content = file_processor.process_text(text)
            elif choice == "2":
                url = input("Enter URL to analyze: ")
                content = file_processor.process_url(url)['content']
            elif choice == "3":
                filepath = input("Enter PDF file path: ")
                if os.path.exists(filepath):
                    with open(filepath, 'rb') as file:
                        content = file_processor.process_pdf(file)
                else:
                    print("File not found!")
                    continue
            else:
                print("Invalid option!")
                continue
                
            if content:
                print("\nAnalyzing content...")
                result = research_service.analyze_content(content)
                print("\nResults:")
                print("--------")
                print(result)
                
        except Exception as e:
            print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()