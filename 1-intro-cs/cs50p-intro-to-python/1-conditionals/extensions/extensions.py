filename = input("File name: ").strip()
extension = filename.split(".")[1].lower()

match extension:
    case "gif":
        print("image/gif")
    case "jpeg" | "jpg":
        print("image/jpeg")
    case "png":
        print("image/png")
    case "pdf":
        print("application/pdf")
    case "txt":
        print("text/plain")
    case "zip":
        print("application/zip")
    case _:
        print("application/octet-stream")