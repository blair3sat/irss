ELAPSED_TIME = 10;
SAMP_RATE = 50e5;
START_F = 3.395e6;
STOP_F = 3.874e6;
REP_T = 6;

ts = 0 : 1 / SAMP_RATE : ELAPSED_TIME;
s_c = chirp(ts, START_F, REP_T, STOP_F)';
win = nuttallwin(65536 * 4 * 4 * 4);

jj = 1;
for ii = 1 : length(win) / 2 : length(s_c) - length(win)
  f(:, jj) = mag2db(abs(fftshift(fft(s_c(ii : ii + length(win) - 1) .* win))));
  jj = jj + 1;
end

[i,j] = size(f);
gr = imagesc(linspace(0, ELAPSED_TIME, length(f)),linspace(0, 40, i), f)
set(gca,'YDir','normal')
colormap(hsv)

figure;

delay = SAMP_RATE * 2.5;
s_t = [zeros(delay, 1) ; s_c(delay : length(s_c) - delay)];

jj = 1;
for ii = 1 : length(win) / 2 : length(s_t) - length(win)
  f(:, jj) = mag2db(abs(fftshift(fft(s_t(ii : ii + length(win) - 1) .* win))));
  jj = jj + 1;
end

[i,j] = size(f);
gr = imagesc(linspace(0, ELAPSED_TIME, length(f)),linspace(0, 40, i), f)
set(gca,'YDir','normal')
colormap(hsv)

figure;

[xc, lag] = xcorr(s_t, s_c);
plot(xc);