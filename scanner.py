#!/usr/bin/env python3
import sys
import urllib.request
import urllib.error
from urllib.parse import urlparse

SECURITY_HEADERS = [('Strict-Transport-Security', 'Obriga a utilizacao de ligacoes encriptadas HTTPS (HSTS).'), ('Content-Security-Policy', 'Mitiga ataques de injecao de scripts e XSS.'), ('X-Frame-Options', 'Previne ataques de clickjacking controlando a integracao em frames.'), ('X-Content-Type-Options', 'Impede o browser de executar MIME-sniffing em ficheiros recebidos.'), ('Referrer-Policy', 'Restringe a fuga de parametros sensiveis de URLs entre origens.'), ('Permissions-Policy', 'Bloqueia o acesso indevido a microfone, camara e geolocalizacao.')]

def scan_target(target_url):
    print(f"\n[TAVARDT Portugal] A iniciar auditoria perimetral de cabecalhos de seguranca para: {target_url}\n")
    try:
        req = urllib.request.Request(
            target_url,
            headers={"User-Agent": "TAVARDT-Security-Scanner/3.0 (pt-PT)"}
        )
        with urllib.request.urlopen(req, timeout=12) as response:
            headers = dict(response.headers.items())
            
            score = 0
            total = len(SECURITY_HEADERS)
            
            for header_name, desc in SECURITY_HEADERS:
                found = any(h.lower() == header_name.lower() for h in headers.keys())
                if found:
                    print(f"  [CONFORME] {header_name}")
                    score += 1
                else:
                    print(f"  [AUSENTE] {header_name}: {desc}")
                    
            print(f"\n[TAVARDT Portugal] Pontuacao Final: {score}/{total}")
            print(f"\nVerificacao completa online: https://tools.tavardt.com/pt/analise-cabecalhos-seguranca/")
            print(f"Suporte corporativo e ciberdefesa: https://ag.tavardt.com/pt/ciberseguranca/\n")
            
    except urllib.error.URLError as e:
        print(f"[TAVARDT Portugal] Erro ao inspecionar o alvo: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python scanner.py <URL>")
        sys.exit(1)
        
    url = sys.argv[1].strip()
    if not urlparse(url).scheme:
        url = "https://" + url
        
    scan_target(url)
