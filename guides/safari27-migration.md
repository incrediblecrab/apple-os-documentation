# Safari 27 migration

**Scope:** Web content, embedded WebKit, and Safari extensions; September 14, 2026 release-note review.

## Separate browser, host, and native API versions

The [Safari 27 release notes](https://developer.apple.com/documentation/safari-release-notes/safari-27-release-notes) list Safari 27 for iOS 27, iPadOS 27, visionOS 27, macOS 27, **macOS 26, and macOS Sequoia**. Do not require macOS 27 merely because a person uses Safari 27. Conversely, a newer Safari installation does not prove that a native WebKit 27 symbol is available to an app on an older host.

Test the actual deployment combinations: Safari, Home Screen/Mac web apps, embedded `WKWebView`, and extensions can differ in permissions, data stores, available APIs, and platform interaction. Use capability checks instead of user-agent version branching.

## Preserve native form behavior

Safari 27 adds customizable `<select>`. Keep labels, option values, keyboard operation, validation, and submission in native HTML:

```html
<label for="delivery">Delivery</label>
<select id="delivery" name="delivery" class="delivery-select">
  <option value="standard">Standard delivery</option>
  <option value="express">Express delivery</option>
</select>
```

```css
@supports (appearance: base-select) {
  .delivery-select,
  .delivery-select::picker(select) {
    appearance: base-select;
  }
  .delivery-select::picker-icon {
    color: currentColor;
  }
}
```

Unsupported browsers retain their native selector. Add `<selectedcontent>` or richly structured options only with a tested fallback; do not replace a working control with a JavaScript imitation solely for styling.

## Recheck scrolling and positioned UI

- **Scroll anchoring** is enabled by default (`overflow-anchor: auto`). Exercise feeds where images or older messages load above the viewport. Remove duplicate application scroll compensation only after testing; use `overflow-anchor: none` narrowly where the application intentionally owns positioning.
- **Anchor positioning** follows transformed anchors in Safari 27. Test moving/scaled triggers, popovers, clipping, and fallback positions. `position-anchor: normal` is the new default, behaving as `auto` with `position-area` and otherwise as `none`; explicit `none` opts out of a default anchor. `position-visibility: anchor-valid` and `anchor-visible` replace the plural keywords, which remain compatibility aliases.
- **Grid Lanes is not new to Safari 27:** the [WebKit field guide](https://gridlanes.webkit.org/) lists Safari 26.4+. Its syntax is `display: grid-lanes` with `grid-template-columns` or `grid-template-rows`, not `display: masonry` or `grid-template-rows: masonry`.

```css
.cards {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 1rem;
}
@supports (display: grid-lanes) {
  .cards {
    display: grid-lanes;
    flow-tolerance: 1em;
  }
}
```

Keep meaningful source order and test keyboard/reading order as items pack into lanes. The regular Grid layout is an intentional fallback, not an error.

## JavaScript, Wasm, and announcements

Safari 27 fixes module-loader ordering around top-level `await` and adds WebAssembly JavaScript Promise Integration. Detect both entry points before selecting a JSPI-enabled build:

```js
const supportsJSPI =
  typeof WebAssembly !== "undefined" &&
  typeof WebAssembly.Suspending === "function" &&
  typeof WebAssembly.promising === "function";

const supportsAnnouncements =
  typeof document !== "undefined" &&
  typeof document.ariaNotify === "function";
```

Keep the existing non-JSPI loading path for unsupported runtimes. JSPI suspends Wasm around Promise-producing imports and resumes through the event queue; the underlying network I/O stays asynchronous.

For announcements not represented by DOM changes, use `document.ariaNotify(message)` when supported. Otherwise update an established `role="status"`/`aria-live` region. Do not announce the same event through both mechanisms, and do not add announcements for content already conveyed by focus or live-region changes. Respect the `aria-notify` Permissions Policy: a function's presence does not guarantee delivery. Test with VoiceOver, not just a successful feature check. The guard above also works in extension workers without a `document`; perform DOM announcements in an appropriate document context.

## Spatial content, embedding, and extensions

- Safari 27 expands `<model>` to iOS/iPadOS/macOS. Immersive website environments and spatial/panorama `<img controls>` are visionOS 27 features. Offer a useful image/text fallback and verify the specific interaction API before showing an immersive action.
- For native apps, gate [WebKit 27 symbols](../documentation/WebKit.md#native-embedding-apis) with platform availability. The SwiftUI-facing `WebView`/`WebPage` APIs instead start at OS 26. Validate navigation policy, content-world messaging, cookie isolation, and authentication flows independently of browser CSS support.
- Safari 27 web extensions gain `runtime.getDocumentId()`, exception reporting, and user-activation propagation through `sendMessage()`, `connect()`, `postMessage()`, and `executeScript()`. Detect optional APIs and retest content-script permissions and gesture-gated actions.
- The [App Store Connect web-extension packager](https://developer.apple.com/documentation/safariservices/packaging-and-distributing-safari-web-extensions-with-app-store-connect) works from a browser without local Xcode/macOS. It still requires Developer Program enrollment and App Store review. It packages web-extension resources, not arbitrary native Safari app-extension code.

## Release checks

Retest forms with touch/keyboard/VoiceOver; delayed-content scrolling; transformed anchors; module cycles and rejection paths; storage/cookie boundaries; extension updates and disabled permissions. A release-note **resolved issue** is a regression-test target, not an enduring limitation.

## Sources

- [WebKit: Safari 27 developer changes](https://webkit.org/blog/17967/news-from-wwdc26-webkit-in-safari-27-beta/)
- [Web technology sessions at WWDC26](https://webkit.org/blog/17974/web-technology-sessions-at-wwdc26/)
- [Safari 27 release notes](https://developer.apple.com/documentation/safari-release-notes/safari-27-release-notes)
- [CSS appearance definitions](https://drafts.csswg.org/css-ui-4/) and [picker/control styling](https://drafts.csswg.org/css-forms-1/)
- [Grid Lanes field guide](https://gridlanes.webkit.org/) and [progressive-enhancement strategies](https://webkit.org/blog/17758/when-will-css-grid-lanes-arrive-how-long-until-we-can-use-it/)
- [WebAssembly JSPI design](https://github.com/WebAssembly/js-promise-integration/blob/main/proposals/js-promise-integration/Overview.md) and [ARIA notification interface](https://w3c.github.io/aria/#ARIANotifyMixin)
- [Safari developer tools](../documentation/safari-developer-tools.md) and [release index](../documentation/safari-release-notes.md)
