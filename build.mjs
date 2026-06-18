import fs from "node:fs/promises";
import path from "node:path";

const root = process.cwd();
const srcDir = path.join(root, "src");
const publicDir = path.join(root, "public");
const distDir = path.join(root, "dist");

async function copyDir(source, destination) {
  await fs.mkdir(destination, { recursive: true });
  const entries = await fs.readdir(source, { withFileTypes: true });
  for (const entry of entries) {
    const from = path.join(source, entry.name);
    const to = path.join(destination, entry.name);
    if (entry.isDirectory()) {
      await copyDir(from, to);
    } else if (entry.isFile()) {
      await fs.copyFile(from, to);
    }
  }
}

await fs.rm(distDir, { recursive: true, force: true });
await copyDir(srcDir, distDir);
await copyDir(publicDir, distDir);
console.log(`Built static site to ${distDir}`);
