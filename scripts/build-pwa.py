#!/usr/bin/env python3
"""Gera docs/index.html (app instalável) a partir de index.html (fonte única)."""
import pathlib, re, time
root = pathlib.Path(__file__).resolve().parent.parent
src = (root / "index.html").read_text(encoding="utf-8")
title = re.search(r"<title>.*?</title>\n?", src).group(0)
body = src.replace(title, "", 1)
head = f"""<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
{title.strip()}
<meta name="theme-color" content="#efe6d6">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="default">
<meta name="apple-mobile-web-app-title" content="Treino">
<link rel="manifest" href="manifest.webmanifest">
<link rel="icon" type="image/png" sizes="192x192" href="icons/icon-192-v2.png">
<link rel="apple-touch-icon" sizes="180x180" href="icons/apple-touch-icon-v2.png">
<style>:root{{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}}body{{margin:0}}img{{max-width:100%}}</style>
</head>
<body>
"""
tail = """
<script>
if ("serviceWorker" in navigator) addEventListener("load", () => navigator.serviceWorker.register("sw.js").catch(() => {}));
try { navigator.storage && navigator.storage.persist && navigator.storage.persist(); } catch (e) {}
</script>
</body>
</html>
"""
(root / "docs" / "index.html").write_text(head + body + tail, encoding="utf-8")
sw = (root / "docs" / "sw.js")
txt = sw.read_text(encoding="utf-8")
txt = re.sub(r'const VERSION = "[^"]*";', f'const VERSION = "v{int(time.time())}";', txt)
sw.write_text(txt, encoding="utf-8")
print("docs/index.html gerado")
