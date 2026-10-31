// Main thread: xterm.js terminal + keyboard ring buffer shared with the Python worker.
(async () => {
  if (!window.crossOriginIsolated) {
    if (!('serviceWorker' in navigator)) { document.getElementById('status').textContent = 'Navegador sem suporte a Service Worker.'; return; }
    const reg = await navigator.serviceWorker.register('coi-sw.js');
    if (!sessionStorage.getItem('coi-reloaded')) {
      sessionStorage.setItem('coi-reloaded', '1');
      await navigator.serviceWorker.ready;
      location.reload();
      return;
    }
    document.getElementById('status').textContent = 'Não consegui ativar o isolamento (SharedArrayBuffer). Tente recarregar.';
    return;
  }
  sessionStorage.removeItem('coi-reloaded');
  const cfg = window.GAME || {};
  const term = new Terminal({
    cols: cfg.cols || 80, rows: cfg.rows || 30, convertEol: true, cursorBlink: true,
    fontFamily: '"Cascadia Mono", Consolas, "Lucida Console", monospace', fontSize: 15,
    theme: { background: '#000000', foreground: '#c0c0c0', cursor: '#c0c0c0' },
  });
  term.open(document.getElementById('term'));
  term.focus();

  const N = 8192;
  const sab = new SharedArrayBuffer(16 + N);
  const hdr = new Int32Array(sab, 0, 4);
  const data = new Uint8Array(sab, 16, N);
  const enc = new TextEncoder();
  const push = (s) => {
    for (const b of enc.encode(s)) {
      const w = Atomics.load(hdr, 0);
      data[w % N] = b;
      Atomics.store(hdr, 0, w + 1);
    }
    Atomics.notify(hdr, 0);
  };
  term.onData(push);

  const status = document.getElementById('status');
  const worker = new Worker('worker.js');
  worker.onmessage = (e) => {
    const m = e.data;
    if (m.t === 'out') term.write(m.s);
    else if (m.t === 'status') status.textContent = m.s;
    else if (m.t === 'title') document.title = m.s;
  };
  worker.postMessage({ t: 'start', sab, game: cfg, base: location.href.replace(/[^/]*$/, '') });
  document.getElementById('term').addEventListener('click', () => term.focus());
})();
