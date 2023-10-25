% need to save Br from FDIPS in .csv file first
clear; close all;
save_or_not = 0;
%% import data
store_dir = ('E:\Research\Data\SWMF\magnetogram\FDIPS\FDIPS1206\');
file_name = 'Br.csv';
data_dir = [store_dir,file_name];
data = importdata(data_dir);
data = data(2:end,:);
%% extract grid
[num_lat,num_lon] = size(data);
lon = linspace(0,360,num_lon);
lat_sin = linspace(-1,1,num_lat);
lat = asin(lat_sin) * 180 / pi;
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

h = pcolor(lon,lat,data);
set(h,'LineStyle','none');
cb = colorbar;
colormap(red_white_blue);
axis equal
xlim([0 360]);
ylim([-90 90]);
set(gca,'CLim',[-50 50],'TickDir','out','XminorTick','on','YminorTick','on','LineWidth',LineWidth,'FontSize',FontSize);

save_name = 'Based on FDIPS';
title(save_name,'FontSize',FontSize);
if save_or_not == 1
    saveas(gca,[store_dir,save_name,'.png']);
end