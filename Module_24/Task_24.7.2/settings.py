import os

from dotenv import load_dotenv

load_dotenv()

valid_email = os.getenv('valid_email')
valid_password = os.getenv('valid_password')

invalid_email = 'ono@mail.ru'
invalid_password = 'qwerty12345'


name255 = 'LRkKCt3mBg2NQoAk1RXQXXhZAqI5Hd74uvIWFvUblNP3FdbMzfhyK4OQ2wqw8B0g67zxlYD1UYv5j42RzuQROe0dzOELuPRhnN2JDzcg3' \
          '8KXs4AsJ95JCoRQBIqNJ8m7AcznFjpcLubkB832Y8nwBlpgm9JMNrS5Qbl5Q6rMj54QUHZjibaKbywEs6JJRDMrmn60h91pcVHtzDOlSC1' \
          'MIWg0z0sA7zqZImH1SEYtZwOQ6WbIL1IcF0VUWGelDCS'
animal_type255 = 'uB2Q8ivVQVcQOt0urT3GoRvQmlu2w01f0AgWNj0YJNDEfHwPCVZ41JLwPieWhnLyygCeMxN5wzdFhPSm21CXrKKftJTDNd134y' \
                 'Ngv9PNyQupXrNTmcB8l3ijhK7vRILYMkbaHoM56VLKuVpCVPXlzOPx1OjAwhmDNUts4YN5JVHd9Jywwa2q5HfjdXdn0SZPrlF' \
                 'gqk9nWtC6JaH290sMUKoGGCgZTznXYbu80CfPOco2rTPok1RiVZenw33vlUy'


invalid_auth_key = {
  "key": "ea738148a1f19838e1c5d1413877f3691a3731380e733e877b0ae729"
}
