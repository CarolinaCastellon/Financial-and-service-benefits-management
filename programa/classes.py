class User:
    """
    Método constructor para la clase User.

    Args:
        user_id (str): El ID del usuario.
        username (str): El nombre de usuario del usuario.
        email (str): La dirección de correo electrónico del usuario.
        password (str): La contraseña del usuario.
    """
    def __init__(self, user_id, username, email, password):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.password = password
        self.benefits = []

    def add_benefit(self, benefit):
        self.benefits.append(benefit)

class Account:
    """
    Método constructor para la clase Account.

    Args:
        account_id (str): El ID de la cuenta.
        user_id (str): El ID del usuario asociado.
        balance (float): El saldo de la cuenta.
    """
    def __init__(self, account_id, user_id, balance):
        self.account_id = account_id
        self.user_id = user_id
        self.balance = balance
        self.transactions = []

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

class Transaction:
    """
    Método constructor para la clase Transaction.

    Args:
        transaction_id (str): El ID de la transacción.
        account_id (str): El ID de la cuenta asociada.
        amount (float): El monto de la transacción.
        timestamp (datetime): La marca de tiempo de la transacción.
    """
    def __init__(self, transaction_id, account_id, amount, timestamp):
        self.transaction_id = transaction_id
        self.account_id = account_id
        self.amount = amount
        self.timestamp = timestamp

class TransactionHistory:
    """
    Método constructor para la clase TransactionHistory.

    Args:
        user_id (str): El ID del usuario asociado.
        transactions (list): Una lista de transacciones pasadas.
    """
    def __init__(self, user_id, transactions):
        self.user_id = user_id
        self.transactions = transactions


class BenefitTransaction:
    """
    Método constructor para la clase BenefitTransaction.

    Args:
        transaction_id (str): El ID de la transacción.
        user_id (str): El ID del usuario asociado.
        benefit_id (str): El ID del beneficio asociado.
        timestamp (datetime): La marca de tiempo de la transacción.
    """
    def __init__(self, transaction_id, user_id, benefit_id, timestamp):
        self.transaction_id = transaction_id
        self.user_id = user_id
        self.benefit_id = benefit_id
        self.timestamp = timestamp

class BenefitProvider:
    """
    Método constructor para la clase BenefitProvider.

    Args:
        provider_id (str): El ID del proveedor.
        name (str): El nombre del proveedor.
    """
    def __init__(self, provider_id, name):
        self.provider_id = provider_id
        self.name = name
        self.benefits = []

class Benefit:
    """
    Método constructor para la clase Benefit.

    Args:
        benefit_id (str): El ID del beneficio.
        name (str): El nombre del beneficio.
        description (str): La descripción del beneficio.
        value (float): El valor del beneficio.
    """
    def __init__(self, benefit_id, name, description, value):
        self.benefit_id = benefit_id
        self.name = name
        self.description = description
        self.value = value
    
class BenefitPlan:
    """
    Método constructor para la clase BenefitPlan.

    Args:
        plan_id (str): El ID del plan de beneficios.
        name (str): El nombre del plan de beneficios.
        benefits (list): Una lista de beneficios incluidos en el plan.
    """
    def __init__(self, plan_id, name, benefits):
        self.plan_id = plan_id
        self.name = name
        self.benefits = benefits

class Authentication:
    """
    Método constructor para la clase Authentication.

    Args:
        user_id (str): El ID del usuario asociado.
        token (str): El token de autenticación.
        expiry_date (datetime): La fecha de vencimiento del token de autenticación.
    """
    def __init__(self, user_id, token, expiry_date):
        self.user_id = user_id
        self.token = token
        self.expiry_date = expiry_date

class Recommendation:
    """
    Método constructor para la clase Recommendation.

    Args:
        user_id (str): El ID del usuario asociado.
        recommendations (list): Una lista de beneficios recomendados.
    """
    def __init__(self, user_id, recommendations):
        self.user_id = user_id
        self.recommendations = recommendations
