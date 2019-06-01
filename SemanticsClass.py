
class Semantics:
    query = None

    def __init__(self, query):
        self.query = query

    def queryTreatment(self):
        results = []
        if "hash" in self.query:
            query_splitted = self.query.split()
            query_size = len(query_splitted)
            for i in range(0, query_size):
                if "select" in query_splitted[i] or "SELECT" in query_splitted[i] or "Select" in query_splitted[i]:
                    nation_query = query_splitted[i]
                    nflag = 0
                    customer_query = query_splitted[i]
                    cflag = 0
                    lineitem_query = query_splitted[i]
                    lflag = 0
                    orders_query = query_splitted[i]
                    oflag = 0
                    part_query = query_splitted[i]
                    pflag = 0
                    partsupp_query = query_splitted[i]
                    psflag = 0
                    region_query = query_splitted[i]
                    rflag = 0
                    supplier_query = query_splitted[i]
                    sflag = 0
                    for j in range(i, query_size):
                        if "from" in query_splitted[j] or "FROM" in query_splitted[j] or "From" in query_splitted[j]:
                            nation_query += ' ' + "from TPCSOURCE.NATION"
                            supplier_query += ' ' + "from TPCSOURCE.SUPPLIER"
                            customer_query += ' ' + "from TPCSOURCE.CUSTOMER"
                            lineitem_query += ' ' + "from TPCSOURCE.LINEITEM"
                            orders_query += ' ' + "from TPCSOURCE.ORDERS"
                            part_query += ' ' + "from TPCSOURCE.PART"
                            partsupp_query += ' ' + "from TPCSOURCE.PARTSUPP"
                            region_query += ' ' + "from TPCSOURCE.REGION"
                            if nflag != 0:
                                results.append(nation_query)
                            if sflag != 0:
                                results.append(supplier_query)
                            if cflag != 0:
                                results.append(customer_query)
                            if lflag != 0:
                                results.append(lineitem_query)
                            if oflag != 0:
                                results.append(orders_query)
                            if pflag != 0:
                                results.append(part_query)
                            if psflag != 0:
                                results.append(partsupp_query)
                            if rflag != 0:
                                results.append(region_query)
                            return results

                        if "N_" in query_splitted[j]:
                            if nflag >= 1:
                                nation_query += ',' + ' ' + query_splitted[j]
                            else:
                                nation_query += ' ' + query_splitted[j]
                            nflag += 1

                        if "S_" in query_splitted[j] and "PS_" not in query_splitted[j]:
                            if sflag >= 1:
                                supplier_query += ',' + ' ' + query_splitted[j]
                            else:
                                supplier_query += ' ' + query_splitted[j]
                            sflag += 1

                        if "C_" in query_splitted[j]:
                            if cflag >= 1:
                                customer_query += ',' + ' ' + query_splitted[j]
                            else:
                                customer_query += ' ' + query_splitted[j]
                            cflag += 1

                        if "L_" in query_splitted[j]:
                            if lflag >= 1:
                                lineitem_query += ',' + ' ' + query_splitted[j]
                            else:
                                lineitem_query += ' ' + query_splitted[j]
                            lflag += 1

                        if "O_" in query_splitted[j]:
                            if oflag >= 1:
                                orders_query += ',' + ' ' + query_splitted[j]
                            else:
                                orders_query += ' ' + query_splitted[j]
                            oflag += 1

                        if "P_" in query_splitted[j] and "PS_" not in query_splitted[j]:
                            if pflag >= 1:
                                part_query += ',' + ' ' + query_splitted[j]
                            else:
                                part_query += ' ' + query_splitted[j]
                            pflag += 1

                        if "PS_" in query_splitted[j]:
                            if psflag >= 1:
                                partsupp_query += ',' + ' ' + query_splitted[j]
                            else:
                                partsupp_query += ' ' + query_splitted[j]
                            psflag += 1

                        if "R_" in query_splitted[j]:
                            if rflag >= 1:
                                region_query += ',' + ' ' + query_splitted[j]
                            else:
                                region_query += ' ' + query_splitted[j]
                            rflag += 1

        else:
            results.append("1")
            return results


