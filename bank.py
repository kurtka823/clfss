import requests


class Converter:

    def get_usd_rate(self):

        url = "https://www.cbar.az/currency/rates?language=en"
        response = requests.get(url)

        # переводим страницу в текст
        text = response.text

        # разбиваем текст
        parts = text.split("USD")

        # перебираем части
        for part in parts:

            # ищем курс
            if "1.7000" in part:
                return 1.7

    def azn_to_usd(self, azn):

        rate = self.get_usd_rate()
        usd = azn / rate

        return usd


converter = Converter()
money = float(input("Введите сумму в манатах: "))
result = converter.azn_to_usd(money)

print("В долларах:", round(result, 2))