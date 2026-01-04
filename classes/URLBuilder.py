class URLBuilder:
    def __init__(self, type, letter, page):
        self.base_url = "http://abbakker.nl/producten.php"
        self.type = type
        self.letter = letter
        self.page = page
        self.url = self.build()

    def build(self):
        # fallback for biljet type, because it doesn't have a letter at the moment
        if self.type == 'biljet':
            return f"{self.base_url}?type={self.type}&letter=memo&pagina={self.page}"

        return f"{self.base_url}?type={self.type}&letter={self.letter}&pagina={self.page}"

    def get_url(self):
        return self.url

    def set_type(self, type):
        self.type = type
        self.url = self.build()

    def set_letter(self, letter):
        self.letter = letter
        self.url = self.build()

    def set_page(self, page):
        self.page = page
        self.url = self.build()
