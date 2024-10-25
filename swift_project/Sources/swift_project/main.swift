import SwiftUI

@main
struct FinanceTrackerApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
    }
}

struct ContentView: View {
    @StateObject private var viewModel = FinanceTrackerViewModel()
    @State private var description = ""
    @State private var amount = ""
    @State private var date = Date()

    var body: some View {
        NavigationView {
            VStack {
                Form {
                    DatePicker("Date", selection: $date, displayedComponents: .date)
                    TextField("Description", text: $description)
                    TextField("Amount", text: $amount)
                        .keyboardType(.decimalPad)
                    
                    Button(action: {
                        if let amount = Double(amount) {
                            viewModel.addTransaction(date: date, description: description, amount: amount)
                            self.description = ""
                            self.amount = ""
                        }
                    }) {
                        Text("Add Transaction")
                    }
                }
                
                List(viewModel.transactions) { transaction in
                    VStack(alignment: .leading) {
                        Text(transaction.description)
                            .font(.headline)
                        Text("\(transaction.amount, specifier: "%.2f")")
                        Text("\(transaction.date, formatter: itemFormatter)")
                            .font(.subheadline)
                            .foregroundColor(.gray)
                    }
                }
                .navigationTitle("Finance Tracker")
            }
        }
    }
}

private let itemFormatter: DateFormatter = {
    let formatter = DateFormatter()
    formatter.dateStyle = .short
    return formatter
}()
