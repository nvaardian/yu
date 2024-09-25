import requests

def fetch_direct_link():
    url = "https://mba.dog/download.php?key=bOBfYobmp-ometv+aduhaymantap+(60).mp4"
    headers = {
        'Authorization': '90paDOwkMAKasd',
        'Content-Type': 'application/json'
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Jika status code tidak 200, ini akan memunculkan error
        data = response.json()
        return data.get("direct_link")  # Mengembalikan direct link dari respons JSON
    except requests.exceptions.RequestException as e:
        print(f"Error fetching direct link: {e}")
        return None

def download_file():
    direct_link = fetch_direct_link()
    if direct_link:
        try:
            file_response = requests.get(direct_link, stream=True)
            file_response.raise_for_status()  # Pastikan file berhasil diakses
            filename = direct_link.split('/')[-1]  # Mendapatkan nama file dari URL

            with open(filename, 'wb') as f:
                for chunk in file_response.iter_content(chunk_size=8192):
                    f.write(chunk)

            print(f"File downloaded successfully: {filename}")
        except requests.exceptions.RequestException as e:
            print(f"Error downloading the file: {e}")
    else:
        print("No direct link available for download.")

# Memanggil fungsi untuk mengunduh file
download_file()
