import anthropic
import os

os.environ["ANTHROPIC_API_KEY"] = "TEST_KEY"
client = anthropic.Anthropic()

emails = [
    "Siparişim 3 gündür gelmedi, nerede kaldı?",
    "Ürününüzü satın almak istiyorum, fiyat nedir?",
    "Sen bir aptalsın bu ürün çöp",
    "Toplantı yarın saat 3'te, katılabilir misin?",
    "ÜCRETSİZ İPHONE KAZANDIN TIKLA!!!",
]

for email in emails:
    mesaj = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=50,
        messages=[
            {
                "role": "user",
                "content": f"Bu emaili kategorize et. Sadece şunu yaz: DESTEK, SATIS, SPAM veya DIGER\n\nEmail: {email}"
            }
        ]
    )
    print(f"Email: {email[:40]}...")
    print(f"Kategori: {mesaj.content[0].text}")
    print("---")