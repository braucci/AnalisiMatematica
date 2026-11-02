# Analisi Matematica — un corso rigoroso, spiegato passo per passo

Libro di Analisi Matematica Uno, scritto in LaTeX, rilasciato con licenza
**CC BY-SA 4.0** (si veda `LICENSE`).

L'impostazione è quella rigorosa e formale dei corsi universitari; la
particolarità del testo è che **ogni teorema** è presentato secondo uno schema
fisso:

1. **enunciato** (cornice azzurra);
2. **schema dell'enunciato** — ipotesi e tesi esplicitate in modo schematico;
3. **piano d'attacco** (cornice verde) — *come* affronteremo la dimostrazione;
4. **dimostrazione**, con ogni passaggio giustificato da un rimando esplicito
   all'assioma o al risultato che lo autorizza.

Accanto compaiono definizioni, esempi, osservazioni, **note storiche**,
**avvertenze** sugli errori comuni, molte **figure** (TikZ / PGFPlots /
Matplotlib) e riquadri di **codice Python** riproducibili. Alcuni teoremi hanno una
**seconda dimostrazione** («Un'altra via»), e le sottosezioni **Approfondimento**
trattano argomenti complementari (assioma di Dedekind, massimo e minimo limite,
quadratura della parabola, funzioni omogenee, prodotti infiniti…); molti di questi
complementi e numerose note storiche seguono i due volumi di *Analisi Matematica* di
Enrico Giusti.

## Compilazione

Il libro richiede **LuaLaTeX** (per i font OpenType e per il pacchetto
`florilegium`, che disegna in Lua gli ornamenti floreali delle pagine di
apertura dei capitoli). Con una distribuzione TeX completa (MacTeX, TeX Live):

```sh
latexmk -lualatex main        # oppure semplicemente:  make
```

Sono necessari tre passaggi (indice, riferimenti incrociati): `latexmk` li
gestisce da solo. Font usati: TeX Gyre Pagella (+ Pagella Math), TeX Gyre
Heros, DejaVu Sans Mono — tutti inclusi in TeX Live; se Pagella Math non è
disponibile il preambolo ripiega automaticamente su Latin Modern.

Per rigenerare le figure prodotte con Python (cartella `figure/`; gli script
`python/fig_*.py` producono le figure, gli altri riproducono i riquadri di codice
del testo):

```sh
pip install numpy matplotlib sympy scipy
make figure
```

## Struttura del progetto

```
main.tex                      file principale: richiama stile, frontmatter e capitoli
latexmkrc, Makefile           configurazione di compilazione
stile/analisi.sty             layout (margine esterno ampio, stile kaobook), font,
                              colori, pacchetti, macro matematiche
stile/teoremi.sty             ambienti: teorema, definizione, schema (Ipotesi/Tesi),
                              strategia (piano d'attacco), dimostrazione, notastorica,
                              attenzione, idea, esercizio/soluzione, python/risultato
stile/florilegium/            pacchetto florilegium (MIT) per gli ornamenti floreali
frontmatter/copertina.tex     copertina
frontmatter/colophon.tex      colophon e licenza
frontmatter/dedica.tex        dedica
frontmatter/introduzione.tex  introduzione e schema dei teoremi di esistenza
frontmatter/bibliografia.tex  bibliografia
capitoli/cap01-numeri-funzioni.tex   Capitolo 1 — I numeri e le funzioni reali
capitoli/cap01/NN-*.tex       i singoli paragrafi del capitolo 1
capitoli/cap02-complementi.tex       Capitolo 2 — Complementi ai numeri reali
capitoli/cap02/NN-*.tex       i singoli paragrafi del capitolo 2
capitoli/cap03-successioni.tex       Capitolo 3 — Limiti di successioni
capitoli/cap03/NN-*.tex       i singoli paragrafi del capitolo 3
capitoli/cap04-funzioni-continue.tex Capitolo 4 — Limiti di funzioni. Funzioni continue
capitoli/cap04/NN-*.tex       i singoli paragrafi del capitolo 4
capitoli/cap05-derivate.tex          Capitolo 5 — Derivate
capitoli/cap05/NN-*.tex       i singoli paragrafi del capitolo 5
capitoli/cap06-applicazioni-derivate.tex  Capitolo 6 — Applicazioni delle derivate. Studio di funzioni
capitoli/cap06/NN-*.tex       i singoli paragrafi del capitolo 6
capitoli/cap07-funzioni-piu-variabili.tex  Capitolo 7 — Funzioni di più variabili
capitoli/cap07/NN-*.tex       i singoli paragrafi del capitolo 7
capitoli/cap08-integrali-definiti.tex  Capitolo 8 — Integrali definiti
capitoli/cap08/NN-*.tex       i singoli paragrafi del capitolo 8
capitoli/cap09-integrali-indefiniti.tex  Capitolo 9 — Integrali indefiniti
capitoli/cap09/NN-*.tex       i singoli paragrafi del capitolo 9
capitoli/cap10-formula-taylor.tex  Capitolo 10 — La formula di Taylor
capitoli/cap10/NN-*.tex       i singoli paragrafi del capitolo 10
capitoli/cap11-serie.tex      Capitolo 11 — Serie
capitoli/cap11/NN-*.tex       i singoli paragrafi del capitolo 11
figure/                       figure generate dagli script Python
python/                       script Python riportati nel testo (eseguire da Libro/)
```

## Come aggiungere un capitolo

1. Creare `capitoli/capNN-titolo.tex` che inizia con
   `\aperturacapitolo{Titolo}{cap:etichetta}` (questo comando attiva anche
   l'ornamento floreale sulla pagina di apertura) e che richiama i paragrafi
   contenuti in `capitoli/capNN/`.
2. Aggiungere `\input{capitoli/capNN-titolo}` in `main.tex`.

## Ambienti principali (stile/teoremi.sty)

```latex
\begin{teorema}[Nome]\label{teo:x} ... \end{teorema}      % anche proposizione, lemma,
                                                          % corollario, assioma
\begin{definizione}[Nome] ... \end{definizione}
\begin{schema}
  \Ipotesi{...}      % può contenere un itemize
  \Tesi{...}
\end{schema}
\begin{strategia} ... \end{strategia}                     % "Piano d'attacco"
\begin{dimostrazione} ... \end{dimostrazione}
\begin{esempio} / \begin{osservazione} / \begin{esercizio} ... \begin{soluzione}
\begin{notastorica}[Titolo] ... \end{notastorica}
\begin{attenzione}[Titolo] ... \end{attenzione}
\begin{idea}[Titolo] ... \end{idea}
\begin{python}[titolo] codice \end{python}   \begin{risultato} output \end{risultato}
\begin{marginfigure} ... \end{marginfigure}  % figura nel margine esterno (sidenotes)
```

Riferimenti incrociati con `cleveref`: `\cref{teo:x}` produce «Teorema 1.3»,
`\eqref{eq:y}` il numero dell'equazione; agli assiomi si fa riferimento con
`\ref{ass:...}`, che produce «(A1)», «(O3)», ecc.

## Fonti

Marcellini–Sbordone, *Elementi di Analisi Matematica uno*; Giusti, *Analisi
Matematica 1*; Tao, *Analysis I–II*; Paolini, *Analisi Uno* (CC BY-SA), da cui
è ispirata la struttura del progetto.
