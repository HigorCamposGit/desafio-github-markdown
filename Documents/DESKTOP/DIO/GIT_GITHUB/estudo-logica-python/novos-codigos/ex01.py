"""
Exercício 01: Variáveis do tipo String e Lista
Objetivo: Criar uma variável que armazena uma string e uma lista que armazena várias strings,
permitindo a interação do usuário.
"""

def main():
    print("=== Demonstração: String e Lista em Python ===")
    
    # 1. Variável que armazena uma string (Nome do usuário)
    nome_usuario = input("Digite o seu nome: ").strip()
    
    print(f"\nOlá, {nome_usuario}! Agora vamos criar uma lista de suas tecnologias favoritas.")
    
    # 2. Lista que armazena várias strings
    tecnologias = []
    
    for i in range(1, 4):
        tech = input(f"Digite a {i}ª tecnologia que você estuda: ").strip()
        if tech:
            tecnologias.append(tech)
            
    # Exibindo os resultados formatados
    print("\n" + "="*40)
    print(f"-> String armazenada (Nome): {nome_usuario}")
    print(f"-> Lista armazenada de tecnologias: {tecnologias}")
    print(f"-> Total de itens na lista: {len(tecnologias)} tecnologias.")
    print("="*40)

if __name__ == "__main__":
    main()