
class SkillManager:

    def __init__(self) -> None:
        self._candidato_habilidades:dict = {}
        self._requisitos_cargo:dict = {}

    def __repr__(self) -> str:
        return f'SkillManager(cadidato_habilidades={self._candidato_habilidades}, requisitos_cargo={self._requisitos_cargo})'

    def adicionar_candidato(self,nome:str, habilidades:set):
        if isinstance(nome,str) and isinstance(habilidades,set):
            self._candidato_habilidades[nome] = habilidades
        else:
            raise TypeError(
                f"""Invalid type for nome or habilidades parameters: nome: {type(nome)}, habilidades: {type(habilidades)}. Expected str(nome) and set(habilidades)"""
            )

    def adicionar_cargo(self,nome:str, requisitos:set):
        if isinstance(nome,str) and isinstance(requisitos,set):
            self._requisitos_cargo[nome] = requisitos
        else:
            raise TypeError(
                f"""Invalid type for nome or habilidades parameters: nome: {type(nome)}, requisitos: {type(requisitos)}. Expected str(nome) and set(requisitos)"""
            )

    def verificar_compatibilidade(self,candidato:str,cargo:str):
        return {"habilidades_em_comum": self._candidato_habilidades[candidato] & self._requisitos_cargo[cargo],
                "habilidades_faltantes": self._requisitos_cargo[cargo] - self._candidato_habilidades[candidato]}

    def listar_todos_candidatos(self):
        return self._candidato_habilidades

    def listar_todos_cargos(self):
        return self._requisitos_cargo
    
if __name__=='__main__':
    # Criando uma instancia
    sk = SkillManager()

    # Adicionando um candidato
    sk.adicionar_candidato(
        'João',{'python','javascript'}
    )
    
    # Adicionando um cargo
    sk.adicionar_cargo(
        'Desenvolvedor',{'python','sql','docker'}
    )

    # Listando os candidatos e cargos
    print(f"Cargos: {sk.listar_todos_cargos()}")
    print(f'Candidatos: {sk.listar_todos_candidatos()}')

    # Verificando compatibilidade
    print("Compatibilidades: ",
        sk.verificar_compatibilidade(
            'João','Desenvolvedor'
        )
    )
    
