ELAPSED_TIME = 1;

[fn, pn] = uigetfile('*.iq');
% fullfile(pn, fn);
fid = fopen(fullfile(pn, fn));
% s = fread(fid,inf,'int16');
% s = fread(fid, 50e6 * 6, 'int16');
s = fread(fid, 50e6 * ELAPSED_TIME, 'int16');
fclose(fid);

s_c = complex(s(1:2:end),s(2:2:end));
win = nuttallwin(65536*4*4*4);
f = zeros(length(win),floor(length(s_c)/length(win)/2));
jj = 1;

for ii = 1 : length(win) / 2 : length(s_c) - length(win)
  f(:, jj) = mag2db(abs(fftshift(fft(s_c(ii : ii + length(win) - 1) .* win))));
  jj = jj + 1;
end

[i,j] = size(f);
gr = imagesc(linspace(0, ELAPSED_TIME, length(f)),linspace(0, 40, i), f)
set(gca,'YDir','normal')
title(fn);
colormap(hsv)