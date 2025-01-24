import graphviz

def create_dfa():
    """Kullanıcıdan DFA tanımını alır."""
    print("Deterministik Sonlu Otomat (DFA) Tanımı:")
    states = set(input("Durumları girin (virgülle ayrılmış): ").split(","))
    alphabet = set(input("Alfabe sembollerini girin (virgülle ayrılmış): ").split(","))
    start_state = input("Başlangıç durumunu girin: ")
    accept_states = set(input("Kabul durumlarını girin (virgülle ayrılmış): ").split(","))
    
    transitions = {}
    print("Geçiş fonksiyonlarını girin (şekil: durum, sembol -> hedef_durum):")
    while True:
        transition = input("Geçiş (ör: q0,a -> q1 veya bitirmek için 'bitir'): ")
        if transition.lower() == 'bitir':
            break
        try:
            parts = transition.split(" -> ")
            source, symbol = parts[0].split(",")
            target = parts[1]
            transitions[(source.strip(), symbol.strip())] = target.strip()
        except:
            print("Geçersiz giriş, doğru formatı kullanın.")

    return {
        "states": states,
        "alphabet": alphabet,
        "start_state": start_state,
        "accept_states": accept_states,
        "transitions": transitions,
    }

def simulate_dfa(dfa, input_string):
    """Verilen DFA ile bir girdiyi simüle eder."""
    current_state = dfa["start_state"]
    for symbol in input_string:
        if (current_state, symbol) in dfa["transitions"]:
            current_state = dfa["transitions"][(current_state, symbol)]
        else:
            return False
    return current_state in dfa["accept_states"]

def visualize_dfa(dfa):
    """DFA'yı görselleştirir."""
    dot = graphviz.Digraph(format='png')
    dot.attr(rankdir='LR')

    # Durumları ekle
    for state in dfa["states"]:
        if state in dfa["accept_states"]:
            dot.node(state, shape='doublecircle')
        else:
            dot.node(state, shape='circle')

    # Geçişleri ekle
    for (source, symbol), target in dfa["transitions"].items():
        dot.edge(source, target, label=symbol)

    # Başlangıç durumunu belirt
    dot.node("start", shape="plaintext", label="")
    dot.edge("start", dfa["start_state"])

    # Görselleştir
    dot.render("dfa_diagram", view=True)

def main():
    dfa = create_dfa()
    
    while True:
        print("\n1. Girdi Simülasyonu")
        print("2. DFA Görselleştirme")
        print("3. Çıkış")
        choice = input("Seçiminizi yapın: ")

        if choice == "1":
            input_string = input("Girdiyi girin: ")
            result = simulate_dfa(dfa, input_string)
            if result:
                print(f"Girdi '{input_string}' kabul edildi.")
            else:
                print(f"Girdi '{input_string}' reddedildi.")
        elif choice == "2":
            visualize_dfa(dfa)
        elif choice == "3":
            print("Çıkış yapılıyor...")
            break
        else:
            print("Geçersiz seçim. Tekrar deneyin.")

if __name__ == "__main__":
    main()
