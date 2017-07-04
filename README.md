<h2><strong>pytune</strong></h2>
<p>&nbsp;</p>
<p>Real-time guitar tuner in Python. For 6-string guitar in D tuning, but it's easy to change.</p>
<p>&nbsp;</p>
<p>Using PyAudio for audio stream and tkinter for interface.</p>
<p>Also using threading and numpy.</p>
<p>&nbsp;</p>
<p>How it looks:</p>
<p><img src="https://lh3.googleusercontent.com/8fc2FPphzK2evnHuPBTjbneB9Ai7LnZtE0QnftZ-5r7J0dAGjSP0SU6a2HamS7VBHsb980S6sf6JRPEpSDY5RjscFJDD3j3rORauRi121E8w2uI7y4Ly8jKnDjWbaFy633SxigI5rDid2FOeF_BkInkMjeGxvYb_mzgSpDUzSPUQTZhJ2GMW_-xUhLvWFqvBrJxSXXiLfSiU-VZTIVrcsI_esKvSwB0KtCe3iA-PnL37ePnnR418hZdcwLuuhbjq98r8CzOvsZVFAHTGxY-Ta1EHRHEJf-f3gQbQ0hXXp2J7BrCmkZ4UslPXFtRIz98p892ExcyfG5UFG7gmzaRjWJKnG2CHTfV6FtJTve1lLtK6ZI-fslY68oy2zbYgo-fWX_BemKjpu70n_tBIiVsqE4lg4LH9A9heNs2UQs8qCq8476eXD_nd6FI7psHHtxNiDIAbQY0hxGEWYDLFLnpfm56lRjLixoVZ8ipY5kbA3FFF9b2M9vvXwpFkl9lFXIS7I1iZ3iwyQfpJNqBb_d9Z85cRJCwko7_xwRaDw8PWCfscVQdzLEA0Ls6JBM81Ti6xBBCkU4kSrNqk2i2hDLPQ15Cf1jgikOalIMUxO4yujoEqwETNAbg2=w448-h139-no" alt="" width="448" height="139" /></p>
<p>&nbsp;</p>
<p>Files:</p>
<p><a id="a084b794bc0759e7a6b77810e01874f2-cd56578a9cfff4460e747ab54b53f6bfeea21128" class="js-navigation-open" title=".gitignore" href="https://github.com/svartmetall/pytune/blob/master/.gitignore">.gitignore</a>&nbsp;- may remain without explanation)</p>
<p><a id="2433b4d6e998f50c28f7521fb8deeda1-c5d3cf1c827ae78f41e3b0e6f79ed6db9568a6ff" class="js-navigation-open" title="audio_freq.py" href="https://github.com/svartmetall/pytune/blob/master/audio_freq.py">audio_freq.py</a>&nbsp;-&nbsp;works with audio stream and wraps frequency into note name.</p>
<p><a id="96af9f914f65fd5e0df0468fdfb784a8-a481b97b4f84fd4199360c511517a5cf22d2a664" class="js-navigation-open" title="digital-7.mono.ttf" href="https://github.com/svartmetall/pytune/blob/master/digital-7.mono.ttf">digital-7.mono.ttf</a>&nbsp;- chosen font.&nbsp;May be changed to another but necessarily with the same width of characters.</p>
<p><a id="0d64677220e4d63df247c97eb5f55f0d-462e0d2a3c8abff64b8d7e2ecc02aa5132c586c1" class="js-navigation-open" title="get_note.py" href="https://github.com/svartmetall/pytune/blob/master/get_note.py">get_note.py</a>&nbsp;- gives note name to frequency.</p>
<p><a id="f35b3b261f66baec46602878b964acc5-9b9776ea1e3d22ab682d911f633e62b7455d19fb" class="js-navigation-open" title="pytune.py" href="https://github.com/svartmetall/pytune/blob/master/pytune.py">pytune.py</a>&nbsp;- run this for tune your guitar.</p>
<p><a id="b4ef698db8ca845e5845c4618278f29a-de353490d73907b2de62a88244e9030ec784ff19" class="js-navigation-open" title="requirements.txt" href="https://github.com/svartmetall/pytune/blob/master/requirements.txt">requirements.txt</a>&nbsp;- required non-standard libraries.</p>
<p><a id="97899de33632ce8bd8e732e2e6910bda-d3a1c4ba0a6b9981dfde65aad4f6561aefbefa3e" class="js-navigation-open" title="widget.py" href="https://github.com/svartmetall/pytune/blob/master/widget.py">widget.py</a>&nbsp;- window interface.</p>
<p>&nbsp;</p>
<p>It also creates freqs.txt in project directory for saving and reading current frequency from audio stream.</p>
<p>I could not think of a better option yet.</p>
<p>&nbsp;</p>
<p>Most of audioworks are from here:&nbsp;<span class="repo js-repo" title="python-tuner"><a class="text-bold" href="https://github.com/mzucker/python-tuner">python-tuner</a>.&nbsp;</span>Thanks!</p>
<p>Sorry for comments in ukrainian, they are mostly for me)</p>
