clear; close all;
save_or_not = 0;
%% import data
store_dir = ('E:\Research\Data\SWMF\magnetogram\');
% file_name = 'CR2239_GNG_modify.dat';
file_name = 'CR2077_GNG_modify.dat';
% file_name = 'CR2077_MDI_180_modify.dat';
data_dir = [store_dir,file_name];
data = load(data_dir);
g = data(:,3);% coeff of cos
h = data(:,4);% coeff of sin
%% extract grid
theta0 = linspace(0,pi,180); % co-latitude
phi0 = linspace(0,2*pi,360); % longitude
lon = phi0./pi.*180;
lat = (pi/2 - theta0)./pi.*180;
n_lim = 180; % max limitation of spherical order
n_max = 30; % max value of spherical order
%% spherical harmonic functions
magneto = zeros(180,360);
for i_n = 0 : n_max % order of harmonics
    % modified from 'sch ' option of matlab legendre function
    P = legendre(i_n,cos(theta0),'sch'); % /sqrt(2*pi);
    temp = (i_n + 1)*i_n/2 + 1;
    for i_m = 1 : i_n + 1 % degree of harmonics
        i_row = temp + i_m - 1;
%         renorm = sqrt(2*i_n + 1);
        renorm = 1; % already normed
        m = i_m - 1;
        triang = g(i_row)*cos(m*phi0) + h(i_row)*sin(m*phi0);
        magneto = magneto + renorm*P(i_m,:).'*triang;
    end
end
magneto = magneto + 2.5; % Notice that C00 is -2.5 relative PREM model
%% colorbar red-white-blue
color_red   = [1,0,0];
color_white = [1,1,1];
color_blue  = [0,0,1];
n1 = 100;
n2 = 100;
R_comp = [linspace(color_red(1),color_white(1),n1),linspace(color_white(1),color_blue(1),n2)];
G_comp = [linspace(color_red(2),color_white(2),n1),linspace(color_white(2),color_blue(2),n2)];
B_comp = [linspace(color_red(3),color_white(3),n1),linspace(color_white(3),color_blue(3),n2)];
red_white_blue = [R_comp',G_comp',B_comp'];
%% plot magnetogram
figure();
LineWidth = 2;
FontSize = 15;

h = pcolor(lon,lat,magneto);
set(h,'LineStyle','none');
cb = colorbar;
colormap(red_white_blue);
axis equal
xlim([0 360]);
ylim([-90 90]);
set(gca,'CLim',[-50 50],'TickDir','out','XminorTick','on','YminorTick','on','LineWidth',LineWidth,'FontSize',FontSize);

save_name = ['Based on ',file_name(8:10),' of Order ',num2str(n_max)];
title(save_name,'FontSize',FontSize);
if save_or_not == 1
    saveas(gca,[store_dir,save_name,'.png']);
end