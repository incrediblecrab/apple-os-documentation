import SwiftUI

@available(iOS 26.0, macOS 26.0, *)
struct LiquidGlassExample: View {
    @Namespace private var namespace

    var body: some View {
        GlassEffectContainer {
            HStack {
                Text("Landmarks")
                    .padding()
                    .glassEffect(.regular, in: .rect(cornerRadius: 20))
                    .glassEffectID("title", in: namespace)
                Button("Explore") {}
                    .buttonStyle(.glassProminent)
            }
        }
    }
}
