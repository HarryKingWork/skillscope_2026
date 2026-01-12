import time
import logging
from datetime import datetime
from typing import List, Dict, Any

# Configure logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class TransactionAnalysis:
    def __init__(self):
        self.transactions = []
    
    def add_transaction(self, transaction: Dict[str, Any]) -> None:
        """
        Adds a new transaction to the list.
        
        :param transaction: Dictionary containing transaction details.
        """
        self.transactions.append(transaction)
        logging.info(f"Transaction added: {transaction}")
    
    def get_transaction_count(self) -> int:
        """
        Returns the total number of transactions.
        
        :return: Total number of transactions.
        """
        return len(self.transactions)
    
    def get_failed_transactions(self) -> List[Dict[str, Any]]:
        """
        Filters and returns all failed transactions.
        
        :return: List of failed transactions.
        """
        failed_transactions = [txn for txn in self.transactions if txn['status'] == 'failed']
        logging.info(f"Found {len(failed_transactions)} failed transactions.")
        return failed_transactions
    
    def calculate_average_response_time(self) -> float:
        """
        Calculate the average response time of all transactions.
        
        :return: Average response time in milliseconds.
        """
        total_time = sum(txn['response_time'] for txn in self.transactions)
        avg_time = total_time / len(self.transactions) if self.transactions else 0
        logging.info(f"Average response time: {avg_time} ms")
        return avg_time
    
    def get_slow_transactions(self, threshold: float) -> List[Dict[str, Any]]:
        """
        Returns transactions with response time greater than the threshold.
        
        :param threshold: Response time threshold in milliseconds.
        :return: List of slow transactions.
        """
        slow_transactions = [txn for txn in self.transactions if txn['response_time'] > threshold]
        logging.info(f"Found {len(slow_transactions)} transactions that exceeded the threshold of {threshold} ms.")
        return slow_transactions
    
    def get_transaction_statistics(self) -> Dict[str, Any]:
        """
        Get statistics like average response time, count of failed transactions, and total transactions.
        
        :return: Dictionary containing statistics.
        """
        stats = {
            "total_transactions": self.get_transaction_count(),
            "failed_transactions": len(self.get_failed_transactions()),
            "average_response_time": self.calculate_average_response_time(),
        }
        logging.info(f"Transaction Statistics: {stats}")
        return stats

    def generate_transaction_report(self) -> str:
        """
        Generates a formatted report of transaction performance.
        
        :return: Formatted transaction report.
        """
        stats = self.get_transaction_statistics()
        report = f"""
        Transaction Report:
        --------------------
        Total Transactions: {stats['total_transactions']}
        Failed Transactions: {stats['failed_transactions']}
        Average Response Time: {stats['average_response_time']} ms
        """
        logging.info("Transaction report generated.")
        return report

    def log_transaction(self, user_id: int, transaction_type: str, response_time: float, status: str) -> None:
        """
        Logs a single transaction.
        
        :param user_id: ID of the user.
        :param transaction_type: Type of the transaction (e.g., 'login', 'purchase').
        :param response_time: Time taken for the transaction in milliseconds.
        :param status: Status of the transaction (e.g., 'success', 'failed').
        """
        transaction = {
            "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "user_id": user_id,
            "transaction_type": transaction_type,
            "response_time": response_time,
            "status": status
        }
        self.add_transaction(transaction)