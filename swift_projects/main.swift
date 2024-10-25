import Foundation

struct Transaction {
    let date: Date
    let description: String
    let amount: Double
}

class FinanceTracker {
    var transactions: [Transaction] = []
    
    func addTransaction(date: Date, description: String, amount: Double) {
        let transaction = Transaction(date: date, description: description, amount: amount)
        transactions.append(transaction)
        print("Transaction added: \(transaction)")
    }
    
    func showTransactions() {
        for transaction in transactions {
            print("\(transaction.date) - \(transaction.description) - \(transaction.amount)")
        }
    }
}

let tracker = FinanceTracker()
tracker.addTransaction(date: Date(), description: "Lunch", amount: 15.50)
tracker.showTransactions()
