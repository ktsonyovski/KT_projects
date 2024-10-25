import Foundation

struct Transaction: Identifiable {
    let id = UUID()
    let date: Date
    let description: String
    let amount: Double
}
