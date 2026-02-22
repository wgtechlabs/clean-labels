import { defineConfig } from 'vite';

export default defineConfig({
  base: '/clean-labels/',
  build: {
    outDir: 'dist',
    emptyOutDir: true,
  },
});
