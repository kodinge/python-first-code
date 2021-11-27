import latest_earthquake

if __name__ == '__main__':
    print('Aplikasi utama')
    result = latest_earthquake.ekstraksi_data()
    latest_earthquake.tampilkan_data(result)