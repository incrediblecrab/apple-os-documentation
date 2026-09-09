final class Observer {}

struct Subscription {
    weak let observer: Observer?

    init(observer: Observer) {
        self.observer = observer
    }
}
