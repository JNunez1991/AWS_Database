USE INE;

-- Data en "t_ipc"
SELECT
	ipc.Periodo,
	ipc.Division,
	dipc.Descripcion,
	ipc.Ponderacion,
	ipc.Indice,
	ipc.Var_mensual,
	ipc.Var_ac_anual,
	ipc.Var_doce_meses,
	ipc.Incidencia

FROM
	t_ipc ipc inner join t_desc_ipc dipc on ipc.Division = dipc.Division;


-- Data en "t_ims"
SELECT
	ims.Periodo,
	ims.Sector,
	dims.Descripcion,
	ims.Indice,
	ims.Mes,
	ims.AcumuladoAnual,
	ims.UltimosDoceMeses,
	ims.Incidencias

FROM
	t_ims ims inner join t_desc_ims dims on ims.Sector = dims.Sector;


-- Data en "t_iccv"
SELECT
	iccv.Periodo,
	iccv.Rubro,
	diccv.Descripcion,
	iccv.Indice,
	iccv.VariacionMensual,
	iccv.Incidencias

FROM
	t_iccv iccv inner join t_desc_iccv diccv on iccv.Rubro = diccv.Rubro;