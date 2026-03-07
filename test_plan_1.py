import re
import pytest
from playwright.sync_api import Page, expect

## Verifica se o sistema retorna a tela inicial em caso de login inválido.
def test_invalid_account(page: Page) -> None:
    page.goto("https://qa-play-sim.lovable.app/")
    page.get_by_role("textbox", name="seu@email.com").click()
    page.get_by_role("textbox", name="seu@email.com").fill("teste@teste.com")
    page.get_by_role("textbox", name="seu@email.com").press("Tab")
    page.get_by_role("textbox", name="••••••••").fill("12345678@")
    page.get_by_role("textbox", name="••••••••").press("Enter")
    page.once("dialog", lambda dialog: dialog.dismiss())
    page.get_by_role("button", name="Entrar").click()
    expect(page.get_by_text("Bem-vindo de voltaEntre com suas credenciais para acessarEmailSenhaA senha")).to_be_visible()

# Verifica se uma conta recem criada pode acessar a página
def test_valid_account_login(page: Page) -> None:
    page.goto("https://qa-play-sim.lovable.app/")
    page.get_by_role("link", name="Criar conta").click()
    page.get_by_role("textbox", name="Seu nome").click()
    page.get_by_role("textbox", name="Seu nome").fill("testnew@gmail.com")
    page.get_by_role("textbox", name="(00) 00000-").click()
    page.get_by_role("textbox", name="(00) 00000-").fill("111111111111")
    page.get_by_role("textbox", name="seu@email.com").click()
    page.get_by_role("textbox", name="seu@email.com").fill("testnew@gmail.com")
    page.get_by_role("textbox", name="seu@email.com").press("Tab")
    page.get_by_role("textbox", name="••••••••").first.fill("1234")
    page.get_by_role("textbox", name="••••••••").first.press("Tab")
    page.get_by_role("textbox", name="••••••••").nth(1).fill("1234")
    page.get_by_role("button", name="Criar conta").click()
    page.get_by_role("button", name="Sair da conta").click()
    page.get_by_role("textbox", name="seu@email.com").click()
    page.get_by_role("textbox", name="seu@email.com").fill("testnew@gmail.com")
    page.get_by_role("textbox", name="••••••••").click()
    page.get_by_role("textbox", name="••••••••").fill("1234")
    page.get_by_role("button", name="Entrar").click()
    expect(page.locator("div").nth(5)).to_be_visible()
    expect(page.locator("#root")).to_match_aria_snapshot("- img \"4blue\"\n- img\n- heading \"Login realizado com sucesso\" [level=1]\n- paragraph: Você foi autenticado e já pode utilizar o sistema.\n- button \"Sair da conta\"")
