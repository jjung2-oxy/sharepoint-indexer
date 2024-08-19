from indexer import SharePointIndexer

def main():
    indexer = SharePointIndexer()
    folder_id = input("Enter the SharePoint folder ID to process: ")
    indexer.process_folder(folder_id)

if __name__ == "__main__":
    main()