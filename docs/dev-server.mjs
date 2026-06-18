import fs from "node:fs/promises";
import http from "node:http";
import path from "node:path";

const root = process.cwd();
const primaryDir = path.join(root, process.argv[2] || "src");
const publicDir = path.join(root, "public");
const requestedPort = Number(process.env.PORT || 4173);

const mimeTypes = new Map([
  [".html", "text/html; charset=utf-8"],
  [".css", "text/css; charset=utf-8"],
  [".js", "text/javascript; charset=utf-8"],
  [".json", "application/json; charset=utf-8"],
  [".svg", "image/svg+xml"],
  [".webp", "image/webp"],
  [".jpg", "image/jpeg"],
  [".png", "image/png"],
]);

async function statFile(filePath) {
  try {
    const stat = await fs.stat(filePath);
    return stat.isFile();
  } catch {
    return false;
  }
}

function safeJoin(base, urlPath) {
  const decoded = decodeURIComponent(urlPath.split("?")[0]);
  const clean = decoded === "/" ? "/index.html" : decoded;
  const filePath = path.normalize(path.join(base, clean));
  return filePath.startsWith(base) ? filePath : null;
}

async function resolveFile(url) {
  const primary = safeJoin(primaryDir, url);
  if (primary && await statFile(primary)) return primary;
  const publicPath = safeJoin(publicDir, url);
  if (publicPath && await statFile(publicPath)) return publicPath;
  return null;
}

const server = http.createServer(async (request, response) => {
  const filePath = await resolveFile(request.url || "/");
  if (!filePath) {
    response.writeHead(404, { "content-type": "text/plain; charset=utf-8" });
    response.end("Not found");
    return;
  }
  const ext = path.extname(filePath);
  response.writeHead(200, {
    "content-type": mimeTypes.get(ext) || "application/octet-stream",
    "cache-control": "no-store",
  });
  response.end(await fs.readFile(filePath));
});

function listen(port) {
  server.once("error", (error) => {
    if (error.code === "EADDRINUSE" && port < requestedPort + 20) {
      listen(port + 1);
      return;
    }
    throw error;
  });
  server.listen(port, "127.0.0.1", () => {
    console.log(`CCE microsite: http://127.0.0.1:${port}`);
  });
}

listen(requestedPort);
