


def create_text_file(kannada_text, file_name):
    with open(file_name + '.txt', 'w', encoding='utf-8') as file:
        # Kannada text to be written to the file
        # kannada_text = "ಹಲೋ, ಈ ಕನ್ನಡ ಪಠ್ಯ ಫೈಲ್ ಆಗಿದೆ! \n ಹಲೋ, ಈ ಕನ್ನಡ ಪಠ್ಯ ಫೈಲ್ ಆಗಿದೆ!"

        # Write Kannada text to the file
        file.write(kannada_text)

    print("Kannada text file created successfully in the name of : ", file_name)


def read_excel():
    import pandas as pd

    # Specify the path to your Kannada Excel file
    excel_file_path = 'kcc_application.xlsx'

    # Read the Excel file into a pandas DataFrame
    df = pd.read_excel(excel_file_path, engine='openpyxl')
    # df.to_excel(excel_file_path, index=False, encoding='utf-8')

    # Display the DataFrame
    df.to_excel('kcc_application1.xlsx')
    print(df)


def create_multiple_kannada_txt_files():
    name = ["aaa", "bbb", "ccc"]
    loan_id = [111, 222, 333]
    for i in range(len(name)):
        kannada_text = f"""
        ಹಲೋ, ಈ ಕನ್ನಡ ಪಠ್ಯ ಫೈಲ್ ಆಗಿದೆ! {name[i]}\n
        ಹಲೋ, ಈ ಕನ್ನಡ ಪಠ್ಯ ಫೈಲ್ ಆಗಿದೆ! {loan_id[i]}\n

        ಹಲೋ ಕನ್ನಡ
        """
        file_name = str(name[i])
        create_text_file(kannada_text, file_name)


def sample_kannada_excel_file():
    import pandas as pd

    # Sample data with Kannada text
    data = {'Name': ['ರಮೇಶ', 'ಲಕ್ಷ್ಮಿ', 'ಗಣೇಶ'],
            'Age': [28, 32, 25],
            'City': ['ಬೆಂಗಳೂರು', 'ಮೈಸೂರು', 'ಹೊಸೂರು']}

    # Create a DataFrame
    df = pd.DataFrame(data)
    df.to_excel('simple.xlsx',index=0)

    # Display the DataFrame
    print(df['Name'][0])
    # print(df['City'])
    print(len(df))

if __name__ == "__main__":
    # sample_kannada_excel_file()
    read_excel()