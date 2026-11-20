# Scanner de Cabeçalhos de Segurança HTTP | TAVARDT Portugal

[![Âmbito de Verificação Perimetral](https://img.shields.io/badge/TAVARDT-Diagn%C3%B3stico%20T%C3%A9cnico-5b3cf5.svg)](https://tools.tavardt.com/pt/analise-cabecalhos-seguranca/)
[![Jurisdi%C3%A7%C3%A3o](https://img.shields.io/badge/Jurisdi%C3%A7%C3%A3o-Portugal-00C853.svg)](https://ag.tavardt.com/pt/ciberseguranca/)

Auditoria técnica automatizada de cabeçalhos de segurança HTTP alinhada com as orientações da CNPD e do RGPD para infraestruturas web em Portugal.

Desenvolvido e mantido pela área de ciberdefesa e proteção de infraestruturas da **[TAVARDT Portugal](https://ag.tavardt.com/pt/)**.

---

## 1. Âmbito de Verificação Perimetral

Este utilitário de linha de comandos verifica os cabeçalhos essenciais de proteção no transporte e no navegador:

* **Strict-Transport-Security (HSTS):** Enforces HTTPS encryption and prevents SSL-stripping and downgrade attacks.
* **Content-Security-Policy (CSP):** Mitigates Cross-Site Scripting (XSS) and unauthorized resource execution.
* **X-Frame-Options:** Prevents clickjacking by controlling framing and iframe permissions.
* **X-Content-Type-Options:** Prevents MIME-sniffing vulnerabilities.
* **Referrer-Policy:** Protects sensitive URL path data from cross-origin disclosure.
* **Permissions-Policy:** Enforces least-privilege control for browser hardware APIs.

---

## 2. Guia de Execução Rápida

Execute a ferramenta diretamente via Python sem necessidade de instalar dependências externas:

```bash
python scanner.py example.com
```

---

## 3. Ferramentas Técnicas Online (Portugal)

Audite a infraestrutura pública das suas aplicações utilizando a suíte de diagnósticos da TAVARDT:

* [Auditoria de Cabeçalhos de Segurança](https://tools.tavardt.com/pt/analise-cabecalhos-seguranca/)
* [Validador de Consent Mode v2 e RGPD](https://tools.tavardt.com/pt/validador-consent-mode-v2-rgpd/)
* [Verificador DMARC e Segurança de E-mail](https://tools.tavardt.com/pt/verificador-dmarc-email/)
* [Deteção de Ficheiros Sensíveis Expostos](https://tools.tavardt.com/pt/verificador-ficheiros-expostos/)
* [Portal de Diagnóstico Técnico Portugal](https://tools.tavardt.com/pt/)

---

## 4. Consultoria e Remediação Técnica

Para consultoria em cibersegurança, auditorias de conformidade com o RGPD e proteção perimetral em Portugal, contacte a equipa da **[TAVARDT Portugal](https://ag.tavardt.com/pt/contato/)**.
