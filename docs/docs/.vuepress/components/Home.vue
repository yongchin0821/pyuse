<template>
  <div>
    <section id="hero">
      <HomeHeroImage />
      <h1 class="tagline">Py<span class="accent">Use</span></h1>

      <p v-if="tagline" class="description">
        {{ tagline }}
      </p>
      <p v-if="tagline2" class="description">
        {{ tagline2 }}
      </p>
      <p v-if="tagline3" class="description">
        {{ tagline3 }}
      </p>

      <p class="actions">
        <a class="get-started" href="/guide/quick_start/"> Get Started -> </a>
        <a class="setup" href="/guide/introduce/">Learn More</a>
      </p>
    </section>
  </div>
</template>

<script setup lang="ts">
import {
  ClientOnly,
  usePageFrontmatter,
  useSiteLocaleData,
  withBase,
} from "@vuepress/client";
import type { FunctionalComponent } from "vue";
import { computed, h } from "vue";
// import { useDarkMode } from "../composables";
const frontmatter = usePageFrontmatter();
const siteLocale = useSiteLocaleData();
// const isDarkMode = useDarkMode();
const heroImage = computed(() => {
  if (frontmatter.value.heroImageDark !== undefined) {
    return frontmatter.value.heroImageDark;
  }
  return frontmatter.value.heroImage;
});
const heroText = computed(() => {
  if (frontmatter.value.heroText === null) {
    return null;
  }
  return frontmatter.value.heroText || siteLocale.value.title || "Hello";
});
const heroAlt = computed(
  () => frontmatter.value.heroAlt || heroText.value || "hero"
);
const tagline = computed(() => {
  if (frontmatter.value.tagline === null) {
    return null;
  }
  return (
    frontmatter.value.tagline ||
    siteLocale.value.description ||
    "Welcome to your VuePress site"
  );
});

const tagline2 = computed(() => {
  if (frontmatter.value.tagline2 === null) {
    return null;
  }
  return frontmatter.value.tagline2;
});

const tagline3 = computed(() => {
  if (frontmatter.value.tagline3 === null) {
    return null;
  }
  return frontmatter.value.tagline3;
});

const HomeHeroImage: FunctionalComponent = () => {
  if (!heroImage.value) return null;
  const img = h("img", {
    src: withBase(heroImage.value),
    alt: heroAlt.value,
  });
  if (frontmatter.value.heroImageDark === undefined) {
    return img;
  }
  // wrap hero image with <ClientOnly> to avoid ssr-mismatch
  // when using a different hero image in dark mode
  return h(ClientOnly, () => img);
};
</script>



<style scoped>
section {
  padding: 42px 32px;
}
#hero {
  padding: 96px 32px;
  text-align: center;
}
.tagline {
  font-size: 90px;
  line-height: 1.25;
  font-weight: 900;
  letter-spacing: -1.5px;
  max-width: 960px;
  margin: 0px auto;
}
html:not(.dark) .accent,
.dark .tagline {
  /* background: -webkit-linear-gradient(315deg, #42d392 25%, #647eff); */
  background: -webkit-linear-gradient(315deg, #FA8072 25%, #8470FF);
  background-clip: text;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}
.description {
  max-width: 960px;
  line-height: 1.5;
  transition: color 2s;
  font-size: 20px;
}
.actions a:not(.get-started) {
  font-size: 16px;
  display: inline-block;
  background-color: var(--c-bg-light);
  padding: 8px 18px;
  font-weight: 500;
  border-radius: 8px;
  transition: background-color 0.5s, color 1s;
}
.actions .icon {
  display: inline;
  position: relative;
  top: -1px;
  margin-left: 2px;
  fill: currentColor;
  transition: transform 0.2s;
}
.actions .get-started:hover {
  transition-duration: 0.2s;
}
.actions .get-started:hover .icon {
  transform: translateX(2px);
}
.actions .setup {
  color: var(--c-text);
}
.actions .setup:hover {
  background-color: #e5e5e5;
  transition-duration: 0.2s;
}
.dark .actions .setup:hover {
  background-color: #3a3a3a;
}

.get-started {
  font-size: 16px;
  display: inline-block;
  border-radius: 8px;
  transition: background-color 0.5s, color 1s;
  position: relative;
  font-weight: 600;
  background-color: #42b883;
  color: #fff;
  margin-right: 18px;
  padding: 8px 18px;
}
.dark .get-started {
  color: #213547;
}
.get-started:hover {
  background-color: #33a06f;
  transition-duration: 0.2s;
}
.dark .get-started:hover {
  background-color: #42d392;
}

/* #highlights {
  max-width: 960px;
  margin: 0px auto;
  color: rgba(60, 60, 60, 0.70);
}
#highlights h2 {
  font-weight: 600;
  font-size: 20px;
  letter-spacing: -0.4px;
  color: var(--vt-c-text-1);
  transition: color 0.5s;
  margin-bottom: 0.75em;
}
#highlights p {
  font-weight: 400;
  font-size: 15px;
}
#highlights .vt-box {
  background-color: transparent;
} */
@media (max-width: 960px) {
  .tagline {
    font-size: 64px;
    letter-spacing: -0.5px;
  }
  .description {
    font-size: 18px;
    margin-bottom: 48px;
  }
}
@media (max-width: 768px) {
  .tagline {
    font-size: 48px;
    letter-spacing: -0.5px;
  }
}
@media (max-width: 576px) {
  #hero {
    padding: 64px 32px;
  }
  .description {
    font-size: 16px;
    margin: 18px 0 30px;
  }
  .actions a {
    margin: 0.5em 0;
  }
}
@media (max-width: 370px) {
  .tagline {
    font-size: 36px;
  }
  .get-started {
    margin-right: 0;
  }
}
</style>
