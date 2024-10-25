import Foundation

class FinanceTrackerViewModel: ObservableObject {
    @Published var transactions: [Transaction] = []
    
    func addTransaction(date: Date, description: String, amount: Double) {
        let transaction = Transaction(date: date, description: description, amount: amount)
        transactions.append(transaction)
    }
}
