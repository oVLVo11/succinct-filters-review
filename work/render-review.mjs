import fs from "fs";
import { marked } from "file:///C:/Users/12116/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/marked/lib/marked.esm.js";

const markdown = fs.readFileSync("drafts/review-integrated.md", "utf8");
const css = `
body { font-family: "Microsoft YaHei", "Noto Sans CJK SC", sans-serif; max-width: 920px; margin: 36px auto; color: #202124; line-height: 1.62; font-size: 14px; }
h1 { font-size: 26px; border-bottom: 2px solid #345; padding-bottom: 10px; }
h2 { font-size: 20px; border-bottom: 1px solid #bbb; padding-bottom: 5px; break-after: avoid; }
h3 { font-size: 16px; break-after: avoid; }
table { border-collapse: collapse; width: 100%; font-size: 11px; }
th, td { border: 1px solid #999; padding: 5px; vertical-align: top; }
th { background: #eef2f5; }
code { font-family: Consolas, monospace; background: #f4f4f4; padding: 1px 3px; }
pre { white-space: pre-wrap; background: #f7f7f7; border-left: 3px solid #789; padding: 8px; break-inside: avoid; }
blockquote { border-left: 4px solid #aaa; margin-left: 0; padding-left: 12px; color: #555; }
a { color: #174ea6; text-decoration: none; }
@media print {
  body { max-width: none; margin: 0; font-size: 10.5pt; }
  h1 { font-size: 20pt; }
  h2 { font-size: 15pt; }
  h3 { font-size: 12pt; }
  table { font-size: 8pt; }
  thead { display: table-header-group; }
  tr { break-inside: avoid; }
  a { color: #000; }
}
`;
const html = `<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><title>Succinct Filters Review v1.0</title><style>${css}</style></head><body>${marked.parse(markdown)}</body></html>`;
fs.writeFileSync("drafts/review-integrated-v1.html", html);
