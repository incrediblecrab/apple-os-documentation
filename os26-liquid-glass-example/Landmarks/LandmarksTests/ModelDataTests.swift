import Foundation
import SwiftUI
import Testing
@testable import Landmarks

@Suite("Landmarks model", .serialized)
@MainActor
struct ModelDataTests {
    @Test func testHostUsesOfflineMode() {
        #expect(ProcessInfo.processInfo.arguments.contains("--offline-demo"))
    }

    @Test func bundledDataLoadsWithoutMapRequests() throws {
        let model = ModelData(loadMapItems: false)
        #expect(!model.landmarks.isEmpty)
        #expect(model.landmarksById.count == model.landmarks.count)
        #expect(model.mapItemsByLandmarkId.isEmpty)
        #expect(model.locationFinder == nil)
        #expect(model.favoritesCollection.isFavoritesCollection)
        let featured = try #require(model.featuredLandmark)
        #expect(model.landmarksById[featured.id] == featured)
    }

    @Test func favoriteToggleRestoresMembership() throws {
        let model = ModelData(loadMapItems: false)
        let landmark = try #require(model.landmarks.first)
        let original = model.isFavorite(landmark)
        defer {
            if model.isFavorite(landmark) != original {
                model.toggleFavorite(landmark)
            }
        }
        model.toggleFavorite(landmark)
        #expect(model.isFavorite(landmark) != original)
        model.toggleFavorite(landmark)
        #expect(model.isFavorite(landmark) == original)
    }

    @Test func collectionsHaveUniqueIDsAndAvoidDuplicateMembers() throws {
        let model = ModelData(loadMapItems: false)
        let landmark = try #require(model.landmarks.first)
        let first = model.addUserCollection()
        let second = model.addUserCollection()
        #expect(first.id != second.id)
        model.add(landmark, to: first)
        model.add(landmark, to: first)
        #expect(first.landmarks.count == 1)
        #expect(model.collectionsContaining(landmark).contains(first))
        model.remove(landmark, from: first)
        #expect(!model.collection(first, contains: landmark))
        model.remove(first)
        #expect(!model.userCollections.contains(first))
    }

    @Test func navigatingBackDismissesInspector() throws {
        let model = ModelData(loadMapItems: false)
        model.path.append(try #require(model.landmarks.first))
        model.isLandmarkInspectorPresented = true
        model.path.removeLast()
        #expect(!model.isLandmarkInspectorPresented)
    }

    @Test func continentGroupingPreservesEveryLandmark() {
        let model = ModelData(loadMapItems: false)
        let grouped = ModelData.Continent.allCases.flatMap { model.landmarks(in: $0) }
        #expect(Set(grouped.map(\.id)) == Set(model.landmarks.map(\.id)))
        #expect(grouped.count == model.landmarks.count)
    }

    @Test func completingAndUndoingActivitiesUpdatesEarnedBadges() throws {
        let model = ModelData(loadMapItems: false)
        var landmark = try #require(model.landmarks.first { $0.badge != nil })
        let badge = try #require(landmark.badge)
        let progress = BadgeProgress(progress: [.takePhoto: false, .readDescription: false])
        landmark.badgeProgress = progress
        model.landmarks = [landmark]
        #expect(model.earnedBadges.isEmpty)
        progress.add(.takePhoto)
        progress.add(.readDescription)
        #expect(model.earnedBadges == [badge])
        progress.remove(.takePhoto)
        #expect(model.earnedBadges.isEmpty)
    }
}
