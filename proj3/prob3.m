clear;
clc;

A = [0,1,2,3,4,5,6];
B =[32,47,65,92,132,190,275];

plot(A,B,'o')

[P]=polyfit(A,log(B),1);

b=P(1);
a=exp(P(2));
func =@(x)(a*exp(b*x));

legend(['a = ',num2str(a),'b = ', num2str(b)])
hold on

fplot(func,[0,6])

hold off