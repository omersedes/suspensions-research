clear;close all;clc;

VF = 56;

shear_rates = load('shear_rates_VF56.txt');

v = VideoWriter('Sigma_Probability_VF56_Normalization1.mp4','MPEG-4');
v.FrameRate = 3;
open(v);

for i = 1:size(shear_rates,1)
   sigma_probability1 = load(['sigma_probability1_VF',num2str(VF,'%g'),'_',num2str(shear_rates(i),'%g'),'cl.txt']);
   index = 2:size(sigma_probability1,2);
   sigma = 10.^((index./10) - 10);
   
   fig = figure(1);hold on; box on;
   l1 =plot(sigma,sigma_probability1(1,2:size(sigma_probability1,2)), 'Marker','o', 'MarkerSize', 6);l1.MarkerFaceColor = l1.Color;
   l2 =plot(sigma,sigma_probability1(2,2:size(sigma_probability1,2)), 'Marker','o', 'MarkerSize', 6);l2.MarkerFaceColor = l2.Color;
   l3 =plot(sigma,sigma_probability1(3,2:size(sigma_probability1,2)), 'Marker','o', 'MarkerSize', 6);l3.MarkerFaceColor = l3.Color;
   l4 =plot(sigma,sigma_probability1(4,2:size(sigma_probability1,2)), 'Marker','o', 'MarkerSize', 6);l4.MarkerFaceColor = l4.Color;
   l5 =plot(sigma,sigma_probability1(5,2:size(sigma_probability1,2)), 'Marker','o', 'MarkerSize', 6);l5.MarkerFaceColor = l5.Color;
   l6 =plot(sigma,sigma_probability1(6,2:size(sigma_probability1,2)), 'Marker','o', 'MarkerSize', 6);l6.MarkerFaceColor = l6.Color;
   l7 =plot(sigma,sigma_probability1(7,2:size(sigma_probability1,2)), 'Marker','o', 'MarkerSize', 6);l7.MarkerFaceColor = l7.Color;
   l8 =plot(sigma,sigma_probability1(8,2:size(sigma_probability1,2)), 'Marker','o', 'MarkerSize', 6);l8.MarkerFaceColor = l8.Color;
   l9 =plot(sigma,sigma_probability1(9,2:size(sigma_probability1,2)), 'Marker','o', 'MarkerSize', 6);l9.MarkerFaceColor = l9.Color;
   
   lgd = legend('Z = 0', 'Z = 1', 'Z = 2', 'Z = 3', 'Z = 4', 'Z = 5', 'Z = 6', 'Z = 7', 'Z = 8');
   lgd.Location = 'northwest';
   title_name = ['$\phi = 0.56 \ \dot{\gamma} =',num2str(shear_rates(i)),'$'];
   title(title_name,'Interpreter','latex');
   xlabel('$\sigma$','Interpreter','latex');
   ylabel('$P(\sigma | Z)$','Interpreter','latex');
   
   ax = gca;ax.FontSize = 16;ax.FontName = 'Times';
   %ax.YScale = 'log';
   ax.XScale = 'log';
   
   ylim([0 0.5]);
   xlim([5e-4 1e3]);
   
   frame = getframe(gcf);
   writeVideo(v,frame);
   close(fig);
   
end

close(v);

v = VideoWriter('Sigma_Probability_VF56_Normalization2.mp4','MPEG-4');
v.FrameRate = 3;
open(v);

for i = 1:size(shear_rates,1)
   sigma_probability1 = load(['sigma_probability2_VF',num2str(VF,'%g'),'_',num2str(shear_rates(i),'%g'),'cl.txt']);
   index = 2:size(sigma_probability1,2);
   sigma = 10.^((index./10) - 10);
   
   fig = figure(1);hold on; box on;
   l1 =plot(sigma,sigma_probability1(1,2:size(sigma_probability1,2)), 'Marker','o', 'MarkerSize', 6);l1.MarkerFaceColor = l1.Color;
   l2 =plot(sigma,sigma_probability1(2,2:size(sigma_probability1,2)), 'Marker','o', 'MarkerSize', 6);l2.MarkerFaceColor = l2.Color;
   l3 =plot(sigma,sigma_probability1(3,2:size(sigma_probability1,2)), 'Marker','o', 'MarkerSize', 6);l3.MarkerFaceColor = l3.Color;
   l4 =plot(sigma,sigma_probability1(4,2:size(sigma_probability1,2)), 'Marker','o', 'MarkerSize', 6);l4.MarkerFaceColor = l4.Color;
   l5 =plot(sigma,sigma_probability1(5,2:size(sigma_probability1,2)), 'Marker','o', 'MarkerSize', 6);l5.MarkerFaceColor = l5.Color;
   l6 =plot(sigma,sigma_probability1(6,2:size(sigma_probability1,2)), 'Marker','o', 'MarkerSize', 6);l6.MarkerFaceColor = l6.Color;
   l7 =plot(sigma,sigma_probability1(7,2:size(sigma_probability1,2)), 'Marker','o', 'MarkerSize', 6);l7.MarkerFaceColor = l7.Color;
   l8 =plot(sigma,sigma_probability1(8,2:size(sigma_probability1,2)), 'Marker','o', 'MarkerSize', 6);l8.MarkerFaceColor = l8.Color;
   l9 =plot(sigma,sigma_probability1(9,2:size(sigma_probability1,2)), 'Marker','o', 'MarkerSize', 6);l9.MarkerFaceColor = l9.Color;
   
   lgd = legend('Z = 0', 'Z = 1', 'Z = 2', 'Z = 3', 'Z = 4', 'Z = 5', 'Z = 6', 'Z = 7', 'Z = 8');
   lgd.Location = 'northwest';
   title_name = ['$\phi = 0.56 \ \dot{\gamma} =',num2str(shear_rates(i)),'$'];
   title(title_name,'Interpreter','latex');
   xlabel('$\sigma$','Interpreter','latex');
   ylabel('$P(\sigma)$','Interpreter','latex');
   
   ax = gca;ax.FontSize = 16;ax.FontName = 'Times';
   %ax.YScale = 'log';
   ax.XScale = 'log';
   
   ylim([0 0.1]);
   xlim([5e-4 1e3]);
   
   frame = getframe(gcf);
   writeVideo(v,frame);
   close(fig);
   
end

close(v);


    