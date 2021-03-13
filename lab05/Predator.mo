model Predator

parameter Real a = 0.7; // коэффициент естественной смертности хищников
parameter Real b = 0.6; // коэффициент естественного прироста жертв
parameter Real c = 0.044; // коэффициент увеличения числа хищников
parameter Real d = 0.022; // коэффициент смертности жертв

//parameter Real x0 = 6.0;// начальная популяция хищников
//parameter Real y0 = 19.0;// начальная популяция жертв

parameter Real x0 = 0.6/0.022;// стационарое состояние хищников (b/d)
parameter Real y0 = 0.7/0.044;// стационарое состояние жертв (a/c)

Real x(start=x0);// популяция хищников
Real y(start=y0);// популяция жертв

equation

der(x) = -a*x + c*x*y;
der(y) = b*y - d*x*y;

end Predator;
