import os
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

def gerar_chave_privada():
    return rsa.generate_private_key(public_exponent=65537, key_size=2048)

def assinar_log(chave_privada, mensagem):
    assinatura = chave_privada.sign(
        mensagem.encode(),
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    return assinatura

if __name__ == "__main__":
    chave_privada = gerar_chave_privada()
    log_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'logs', 'honeypot.log')

    with open(log_path, 'r') as f:
        conteudo = f.read()

    assinatura = assinar_log(chave_privada, conteudo)

with open('../logs/honeypot_signature.sig', 'wb') as sig_file:
    sig_file.write(assinatura)

print("Log assinado e guardado em honeypot_signature.sig")
