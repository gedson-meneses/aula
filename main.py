def adicionar_paciente(pacientes):
  cpf = input("CPF: ")
  if cpf in pacientes:
      print("Operação falhou: paciente já cadastrado.")
      return
  nome = input("Nome: ")
  idade = input("Idade: ")
  endereco = input("Endereço: ")
  telefone = input("Telefone: ")

  if not all([cpf, nome, idade, endereco, telefone]):
      print("Por favor, preencha todos os campos obrigatórios.")
      return

  pacientes[cpf] = {
      "nome": nome,
      "idade": idade,
      "endereco": endereco,
      "telefone": telefone
  }
  print("Novo paciente cadastrado com sucesso!")


def adicionar_medico(medicos):
  crm = input("CRM: ")
  if crm in medicos:
      print("Operação falhou: médico já cadastrado.")
      return
  nome = input("Nome: ")
  especialidade = input("Especialidade: ")
  telefone = input("Telefone: ")

  if not all([crm, nome, especialidade, telefone]):
      print("Por favor, preencha todos os campos obrigatórios.")
      return

  medicos[crm] = {
      "nome": nome,
      "especialidade": especialidade,
      "telefone": telefone
  }
  print("Novo médico cadastrado com sucesso!")


def pesquisar_paciente(pacientes):
  cpf = input("CPF: ")
  paciente = pacientes.get(cpf)
  if paciente:
      print(f"Paciente encontrado: {paciente}")
  else:
      print("Operação falhou: paciente não encontrado.")


def pesquisar_medico(medicos):
  crm = input("CRM: ")
  medico = medicos.get(crm)
  if medico:
      print(f"Médico encontrado: {medico}")
  else:
      print("Operação falhou: médico não encontrado.")


def excluir_paciente(pacientes):
  cpf = input("CPF: ")
  if cpf in pacientes:
      del pacientes[cpf]
      print("Paciente excluído com sucesso!")
  else:
      print("Operação falhou: paciente não encontrado.")


def excluir_medico(medicos):
  crm = input("CRM: ")
  if crm in medicos:
      del medicos[crm]
      print("Médico excluído com sucesso!")
  else:
      print("Operação falhou: médico não encontrado.")


def exibir_menu():
  pacientes = {}
  medicos = {}

  while True:
      print("\nMenu do Sistema")
      print("1. Adicionar Novo Paciente")
      print("2. Adicionar Novo Médico")
      print("3. Pesquisar Paciente por CPF")
      print("4. Pesquisar Médico por CRM")
      print("5. Excluir Paciente pelo CPF")
      print("6. Excluir Médico pelo CRM")
      print("7. Sair do Sistema")

      escolha = input("Escolha uma opção: ")
      if escolha == '1':
          adicionar_paciente(pacientes)
      elif escolha == '2':
          adicionar_medico(medicos)
      elif escolha == '3':
          pesquisar_paciente(pacientes)
      elif escolha == '4':
          pesquisar_medico(medicos)
      elif escolha == '5':
          excluir_paciente(pacientes)
      elif escolha == '6':
          excluir_medico(medicos)
      elif escolha == '7':
          print("Saindo do sistema...")
          break
      else:
          print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
  exibir_menu()