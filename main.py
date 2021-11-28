import latest_earthquake

if __name__ == '__main__':
    Gempa = latest_earthquake.GempaTerkini('https://bmkg.go.id')
    print(Gempa.description)
    Gempa.run()