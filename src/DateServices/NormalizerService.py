from typing import Optional
import re

class Normalizer: 
    months = {
        'jan': '01', 'fev': '02', 'mar': '03', 'abr': '04', 'mai': '05', 'jun': '06',
        'jul': '07', 'ago': '08', 'set': '09', 'out': '10', 'nov': '11', 'dez': '12'
    }

    @classmethod
    def normalize(cls, date: str) -> Optional[str]:
        date = date.replace('.', '')
    
        match = re.match(r'(\d{1,2})\s+de\s+(\w{3,})\s+de\s+(\d{4})', date)
        if not match:
            return None

        day, month_str, year = match.groups()
        month_num = cls.months.get(month_str.lower())

        if not month_num:
            return None

        return f"{year}-{month_num.zfill(2)}-{day.zfill(2)}"