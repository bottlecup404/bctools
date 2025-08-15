import random
import string

def generate_strong_password(length: int = 16) -> str:
    """
    生成强密码
    
    Args:
        length: 密码长度 (默认16)
    
    Returns:
        生成的强密码字符串
    """
    # 定义字符集
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?~"
    
    # 确保每种字符至少出现一次
    password = [
        random.choice(uppercase),
        random.choice(lowercase),
        random.choice(digits),
        random.choice(symbols)
    ]
    
    # 填充剩余字符
    all_chars = uppercase + lowercase + digits + symbols
    password += [random.choice(all_chars) for _ in range(length - 4)]
    
    # 随机打乱顺序
    random.shuffle(password)
    return ''.join(password)