# Scanner de Cabeçalhos de Segurança HTTP | TAVARDT Portugal

[![Âmbito de Verificação Perimetral](https://img.shields.io/badge/TAVARDT-Diagn%C3%B3stico%20T%C3%A9cnico-5b3cf5.svg)](https://tools.tavardt.com/pt/analise-cabecalhos-seguranca/)
Auditoria técnica automatizada de cabeçalhos de segurança HTTP alinhada com as orientações da CNPD e do RGPD para infraestruturas web em Portugal.

Desenvolvido e mantido pela área de ciberdefesa e proteção de infraestruturas da **TAVARDT Portugal**.

***

## 1. Âmbito de Verificação Perimetral

Este utilitário de linha de comandos verifica os cabeçalhos essenciais de proteção no transporte e no navegador:

* **Strict-Transport-Security (HSTS):** Obriga à utilização de ligações encriptadas HTTPS e impede ataques de downgrade e interceção SSL.
* **Content-Security-Policy (CSP):** Mitiga ataques de injeção de scripts (XSS) e restringe as origens autorizadas para carregamento de recursos.
* **X-Frame-Options:** Previne ataques de clickjacking regulando as permissões de incorporação em frames e iframes.
* **X-Content-Type-Options:** Impede a execução indevida de ficheiros derivados de vulnerabilidades de MIME-sniffing.
* **Referrer-Policy:** Protege dados sensíveis contidos em URLs de referência contra fuga para domínios terceiros.
* **Permissions-Policy:** Aplica o princípio do menor privilégio sobre APIs de hardware do navegador (câmara, microfone e geolocalização).

***

## 2. Guia de Execução Rápida

Execute a ferramenta diretamente via Python sem necessidade de instalar dependências externas:

```bash
python scanner.py exemplo.pt
```

***

## 3. Ferramentas Técnicas Online (Portugal)

Audite a infraestrutura pública das suas aplicações utilizando a suíte de diagnósticos da TAVARDT:

* Auditoria de Cabeçalhos de Segurança
* [Validador de Consent Mode v2 e RGPD](https://tools.tavardt.com/pt/validador-consent-mode-v2-rgpd/)
* [Verificador DMARC e Segurança de E-mail](https://tools.tavardt.com/pt/verificador-dmarc-email/)
* [Deteção de Ficheiros Sensíveis Expostos](https://tools.tavardt.com/pt/verificador-ficheiros-expostos/)
* [Portal de Diagnóstico Técnico Portugal](https://tools.tavardt.com/pt/)

***

## 4. Consultoria e Remediação Técnica

Para consultoria em cibersegurança, auditorias de conformidade com o RGPD e proteção perimetral em Portugal, contacte a equipa da **TAVARDT Portugal**.
