ELAPSED_TIME = 5;
SAMP_RATE = 50e6;
START_F = 3.395e6;
STOP_F = 3.874e6 * 8;
REP_T = 6;

% Generate simualated chirp
ts = 0 : 1 / SAMP_RATE : ELAPSED_TIME;
ts = ts(1 : length(ts) - 1);
ch = chirp(ts, START_F, REP_T, STOP_F)';

% Load noise from recording
% [fn, pn] = uigetfile('*.iq');
% fid = fopen(fullfile(pn, fn));
fid = fopen('../data/own/IQREC-02-03-19-13h38m31s479.iq');
s = fread(fid, SAMP_RATE * ELAPSED_TIME * 2, 'int16');
fclose(fid);
s_c = complex(s(1:2:end),s(2:2:end));

% Add them
rep = s_c + ch * 1000;

% Plot them!
win = nuttallwin(65536*4*4*4);
f = zeros(length(win),floor(length(s_c)/length(win)/2));
jj = 1;
for ii = 1 : length(win) / 2 : length(s_c) - length(win)
  f(:, jj) = mag2db(abs(fftshift(fft(rep(ii : ii + length(win) - 1) .* win))));
  jj = jj + 1;
end
[i,j] = size(f);
gr = imagesc(linspace(0, ELAPSED_TIME, length(f)),linspace(0, length(rep) / SAMP_RATE * ELAPSED_TIME, i), f)
set(gca,'YDir','normal')
title(fn);
colormap(hsv)