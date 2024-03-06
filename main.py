from datetime import datetime
from random import randint

# Importar las clases
from classes import User, Account, Transaction, TransactionHistory, BenefitTransaction, BenefitProvider, Benefit,  BenefitPlan, Authentication, Recommendation

def main():
    # Crear objetos de ejemplo para demostrar la funcionalidad del programa
    user1 = User("1", "user1", "user1@example.com", "password123")
    account1 = Account("1", user1.user_id, 1000.0)
    transaction1 = Transaction("1", account1.account_id, 100.0, datetime.now())
    benefit1 = Benefit("1", "Beneficio 1", "Descripción del Beneficio 1", 50.0)
    benefit_transaction1 = BenefitTransaction("1", user1.user_id, benefit1.benefit_id, datetime.now())
    benefit_provider1 = BenefitProvider("1", "Proveedor de Beneficios 1")
    authentication1 = Authentication(user1.user_id, "token123", datetime.now())
    recommendation1 = Recommendation(user1.user_id, [benefit1])
    transaction_history1 = TransactionHistory(user1.user_id, [transaction1])
    benefit_plan1 = BenefitPlan("1", "Plan de Beneficios 1", [benefit1])

    # Agregar beneficios a un usuario
    user1.add_benefit(benefit1)

    # Agregar una transacción a la cuenta del usuario
    account1.add_transaction(transaction1)

    # Imprimir los resultados
    print("Usuario:")
    print("ID:", user1.user_id)
    print("Nombre de Usuario:", user1.username)
    print("Correo Electrónico:", user1.email)
    print("Contraseña:", user1.password)
    print("Beneficios:", [benefit.name for benefit in user1.benefits])
    print()

    print("Cuenta:")
    print("ID de Cuenta:", account1.account_id)
    print("ID de Usuario Asociado:", account1.user_id)
    print("Saldo:", account1.balance)
    print("Transacciones:", [(transaction.transaction_id, transaction.amount) for transaction in account1.transactions])
    print()

    print("Beneficio:")
    print("ID de Beneficio:", benefit1.benefit_id)
    print("Nombre:", benefit1.name)
    print("Descripción:", benefit1.description)
    print("Valor:", benefit1.value)
    print()

    print("Transacción de Beneficio:")
    print("ID de Transacción:", benefit_transaction1.transaction_id)
    print("ID de Usuario:", benefit_transaction1.user_id)
    print("ID de Beneficio:", benefit_transaction1.benefit_id)
    print("Marca de Tiempo:", benefit_transaction1.timestamp)

    print("Proveedor de Beneficios:")
    print("ID de Proveedor:", benefit_provider1.provider_id)
    print("Nombre:", benefit_provider1.name)
    print()

    print("Autenticación:")
    print("ID de Usuario:", authentication1.user_id)
    print("Token:", authentication1.token)
    print("Fecha de Expiración:", authentication1.expiry_date)
    print()

    print("Historial de Transacciones:")
    print("ID de Usuario:", transaction_history1.user_id)
    print("Transacciones:", [(transaction.transaction_id, transaction.amount) for transaction in transaction_history1.transactions])
    print()

    print("Plan de Beneficios:")
    print("ID de Plan de Beneficios:", benefit_plan1.plan_id)
    print("Nombre:", benefit_plan1.name)
    print("Beneficios Incluidos:", [benefit.name for benefit in benefit_plan1.benefits])
    print()

    print("Recomendación:")
    print("ID de Usuario:", recommendation1.user_id)
    print("Beneficios Recomendados:", [benefit.name for benefit in recommendation1.recommendations])

    

# Invocar la función principal
if __name__ == "__main__":
    main()
